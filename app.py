from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app_db = SQLAlchemy(app)


class SalableGood(app_db.Model):
    id = app_db.Column(app_db.Integer(), primary_key=True)
    name = app_db.Column(app_db.String(length=30), nullable=False, unique=True)
    price = app_db.Column(app_db.Integer(), nullable=False)
    barcode = app_db.Column(app_db.String(length=12), nullable=False, unique=True)
    description = app_db.Column(app_db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f"SalableGood {self.name}"


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = SalableGood.query.all()
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    return render_template("market.html", items=items)


if __name__ == '__main__':
    app.run()
