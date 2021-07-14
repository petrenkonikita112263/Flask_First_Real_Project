from flask_login import UserMixin

from market import app_db, app
from market import bcrypt


@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(app_db.Model, UserMixin):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    username = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    user_email = app_db.Column(app_db.String(length=50), nullable=False, unique=True)
    user_pd = app_db.Column(app_db.String(length=60), nullable=False)
    budget = app_db.Column(app_db.Integer(), nullable=False, default=1000)
    items = app_db.relationship("SalableGood", backref="owned_user", lazy=True)

    @property
    def password(self):
        return self.user_pd

    @password.setter
    def password(self, value):
        self.user_pd = bcrypt.generate_password_hash(value).decode("utf-8")

    @property
    def budget_prettify(self):
        if (len(str(self.budget))) >= 4:
            return "{:,.2f}$".format(self.budget)
        else:
            return f"{self.budget}$"

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.user_pd, input_password)


class SalableGood(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    name = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    price = app_db.Column(app_db.Integer(), nullable=False)
    barcode = app_db.Column(app_db.String(length=12), nullable=False, unique=True)
    description = app_db.Column(app_db.String(length=1024), nullable=False, unique=True)
    owner = app_db.Column(app_db.Integer(), app_db.ForeignKey("user.id"))

    def __repr__(self):
        return f"SalableGood {self.name}"
