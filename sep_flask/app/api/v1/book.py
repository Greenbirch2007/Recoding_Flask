
from app.libs.reqprint import Redprint


api = Redprint('book')

@api.route('/get')
def get_book():
    return 'get book'


@api.route('/create')
def create_book():
    return 'create book'