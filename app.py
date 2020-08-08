from flask import Flask
from config import Config
from forms import LoginForm
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__, template_folder="templates")
SECRET_KEY = os.urandom(32)
app.config['SECRET-KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.sqlite3'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

@app.route('/')
def index():
    form = LoginForm()
    return render_template('index.html', title='Sign in', form=form)

@app.route('/login-home')
def login_home():
    return render_template('login-home.html')
