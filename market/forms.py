from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label="username")
    email = StringField(label="email")
    pd = PasswordField(label="password")
    confirm_pd = PasswordField(label="confirm password")
    submit = SubmitField(label="Create Account")
