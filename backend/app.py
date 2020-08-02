from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.sqlite3'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login-home')
def login_home():
    return render_template('login-home.html')

if __name__ == '__main__':
    app.run()

