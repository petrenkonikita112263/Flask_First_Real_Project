from market import app_db


class SalableGood(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    name = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    price = app_db.Column(app_db.Integer(), nullable=False)
    barcode = app_db.Column(app_db.String(length=12), nullable=False, unique=True)
    description = app_db.Column(app_db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f"SalableGood {self.name}"
