from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db  = SQLAlchemy()

def create_app():
	app = Flask(__name__)

	app.config['SECRET_KEY'] = 'secret-key-goes-here'
	app.congi['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	db.init_app(app)

	# blueprint for auth routes in our app
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	# blueprint for non-auth parts of app
	from .main import main as mian_blueprint
	app.register_blueprint(main_blueprint)

	return app