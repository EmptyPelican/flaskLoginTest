from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return 'Index'

@main.route('/profile')
def profile():
	return 'profile'

if __name__ == '__main__':
	main.run(port=8000, host='127.0.0.1')