from flask import Flask
from config import Config
from forms import LoginForm
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
import os

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app = Flask(__name__, template_folder="templates")
csrf = CSRFProtect(app)
SECRET_KEY = 'placeholder'
app.secret_key = SECRET_KEY
csrf.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.sqlite3'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.Model.metadata.reflect(db.engine)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template('index.html', title='Sign in', form=form)

@app.route('/login-home')
def login_home():
    return render_template('login-home.html')
