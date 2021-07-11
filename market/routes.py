from market import app, app_db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import SalableGood, User
from market.forms import RegisterForm


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


@app.route("/registration", methods=["GET", "POST"])
def register_page():
    registration_form = RegisterForm()
    if registration_form.validate_on_submit():
        user_to_create = User(username=registration_form.username.data,
                              user_email=registration_form.email.data,
                              user_pd=registration_form.pd.data)
        app_db.session.add(user_to_create)
        app_db.session.commit()
        return redirect(url_for("market_page"))
    if registration_form.errors != {}:
        for e in registration_form.errors.values():
            flash(f"The error {e} was occurred during registration", category="danger")
    return render_template("register_page.html", form=registration_form)
