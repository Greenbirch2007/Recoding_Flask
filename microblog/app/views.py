from flask import render_template, flash, redirect, url_for, session, g, request
from flask_login import login_user, current_user, login_required, logout_user

from app import app, oid, db
from app.forms import LoginForm
from app.models import User
# 视图函数要有正确的顺序
@app.before_request
def before_request():
    g.user = current_user
#首页视图函数
@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = {'nickname':'Karson'}
    user = g.user
    posts = [{
        'author':{'nickname':'John'},
        'body':'Beautiful day in Portland!'
    },
    {'author':{'nickname':'Susan'},
     'body':'The Avengers movies was so cool!'}
    ]
    return render_template('index.html',title = 'Home',user=user
                           ,posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
        # flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        # return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])


# 用户信息
@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User' + nickname + 'not found.')
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)



def after_login(resp):
    if resp.email is None or resp.email == '':
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user in None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me',None)
    login_user(user,remember_me=remember_me)
    return redirect(request.args.get('next') or url_for('index') )




#登出
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))