from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="username", validators=[Length(min=6, max=30), DataRequired()])
    email = StringField(label="email", validators=[Email(), DataRequired()])
    pd = PasswordField(label="password", validators=[Length(6, ), DataRequired()])
    confirm_pd = PasswordField(label="confirm password", validators=[EqualTo("pd"), DataRequired()])
    submit = SubmitField(label="Create Account")
