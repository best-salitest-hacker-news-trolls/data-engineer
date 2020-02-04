from decouple import config
from flask import Flask, render_template, request


def create_app():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	DB.init_app(app)

	@app.route('/')
	def root():
		DB.create_all()
		users = User.query.all()
		return render_template('base.html', title='Home', users=users)