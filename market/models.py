from market import app_db


class User(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    username = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    user_email = app_db.Column(app_db.String(length=50), nullable=False, unique=True)
    user_pd = app_db.Column(app_db.String(length=60), nullable=False)
    budget = app_db.Column(app_db.Integer(), nullable=False, default=1000)
    items = app_db.relationship("SalableGood", backref="owned_user", lazy=True)


class SalableGood(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    name = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    price = app_db.Column(app_db.Integer(), nullable=False)
    barcode = app_db.Column(app_db.String(length=12), nullable=False, unique=True)
    description = app_db.Column(app_db.String(length=1024), nullable=False, unique=True)
    owner = app_db.Column(app_db.Integer(), app_db.ForeignKey("user.id"))

    def __repr__(self):
        return f"SalableGood {self.name}"