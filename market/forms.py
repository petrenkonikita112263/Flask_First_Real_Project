from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    username = StringField(label="username", validators=[Length(min=6, max=30), DataRequired()])
    email = StringField(label="email", validators=[Email(), DataRequired()])
    pd = PasswordField(label="password", validators=[Length(6, ), DataRequired()])
    confirm_pd = PasswordField(label="confirm password", validators=[EqualTo("pd"), DataRequired()])
    submit = SubmitField(label="Create Account")

    def validate_username(self, username_to_check):
        """Prevent the error from SQLAlchemy, database can have two users with the same username"""
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("The user with this username, has already existed. Type another username.")

    def validate_email(self, email_to_check):
        """Same thing as validate_username but now it's email"""
        user_address = User.query.filter_by(user_email=email_to_check.data).first()
        if user_address:
            raise ValidationError("The user with this email address, has already existed. Type another email address.")


class LoginForm(FlaskForm):
    username = StringField(label="username", validators=[DataRequired()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")


class BoughtItemForm(FlaskForm):
    submit = SubmitField(label="Buy Item")


class SoldItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item")
