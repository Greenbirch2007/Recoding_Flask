
from flask import Flask
from flask_script import Manager,Server,Shell,prompt_bool


app = Flask(__name__)

# from app import app,db,Pa

manager = Manager(app)


def make_shell_context():
    return  {
        'db':db
    }