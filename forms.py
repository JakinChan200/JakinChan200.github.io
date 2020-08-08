from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField('Username', validators=[DataRequired()])
    pw = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')