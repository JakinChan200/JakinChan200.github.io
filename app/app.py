from flask import Flask
from config import Config
from forms import LoginForm
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager, current_user, login_user
# from models import User
import os


app = Flask(__name__, template_folder="templates")
csrf = CSRFProtect(app)
SECRET_KEY = 'placeholder'
app.secret_key = SECRET_KEY
csrf.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.sqlite3'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
db.Model.metadata.reflect(db.engine)

@app.route('/login', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.user.data).first()
        if user is None or not user.check_password(form.pw.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('index.html', title='Sign in', form=form)

@app.route('/login-home')
def login_home():
    return render_template('login-home.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))