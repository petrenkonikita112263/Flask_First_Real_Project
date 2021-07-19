from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from market import app, app_db
from market.forms import RegisterForm, LoginForm, BoughtItemForm, SoldItemForm
from market.models import SalableGood, User


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market", methods=["GET", "POST"])
@login_required
def market_page():
    bought_item_form = BoughtItemForm()
    sold_item_form = SoldItemForm()
    if request.method == "POST":
        # buy item
        bought_item = request.form.get("buy_item")
        item_object = SalableGood.query.filter_by(name=bought_item).first()
        if item_object:
            if current_user.has_enough_money(item_object):
                item_object.own_item(current_user)
                flash(f"Successfully bought {item_object.name}", category="success")
            else:
                flash(f"Unfortunately there's no enough money to buy {item_object.name}. "
                      f"Please add some money to your budget", category="danger")
        # discard bought item
        sold_item = request.form.get("sold_item")
        sold_item_object = SalableGood.query.filter_by(name=sold_item).first()
        if sold_item_object:
            if current_user.has_bought_item(sold_item_object):
                sold_item_object.discard_item(current_user)
                flash(f"Successfully discard the bought operation. "
                      f"The item {sold_item_object.name} is removed from your basket", category="success")
            else:
                flash(f"Unfortunately, you didn't buy {sold_item_object.name}.", category="danger")
        return redirect(url_for("market_page"))
    if request.method == "GET":
        items = SalableGood.query.filter_by(owner=None)
        user_items = SalableGood.query.filter_by(owner=current_user.id)
        return render_template("market.html", items=items, bought_item_form=bought_item_form,
                               user_items=user_items, sold_item_form=sold_item_form)


@app.route("/registration", methods=["GET", "POST"])
def register_page():
    registration_form = RegisterForm()
    if registration_form.validate_on_submit():
        user_to_create = User(username=registration_form.username.data,
                              user_email=registration_form.email.data,
                              password=registration_form.pd.data)
        app_db.session.add(user_to_create)
        app_db.session.commit()
        login_user(user_to_create)
        flash(f"Successfully created account. You're log in as {user_to_create.username}", category="success")
        return redirect(url_for("market_page"))
    if registration_form.errors != {}:
        for e in registration_form.errors.values():
            flash(f"The error {e} was occurred during registration", category="danger")
    return render_template("register_page.html", form=registration_form)


@app.route("/login", methods=["GET", "POST"])
def log_in_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        visited_user = User.query.filter_by(username=login_form.username.data).first()
        if visited_user and visited_user.check_password(input_password=login_form.password.data):
            login_user(visited_user)
            flash(f"Successfully Log In Operation. Hello {visited_user.username}", category="success")
            return redirect(url_for("market_page"))
        else:
            flash("Unfortunately the input data isn't matched with stored in DB", category="danger")
    return render_template("login.html", form=login_form)


@app.route("/logout")
def log_out_page():
    logout_user()
    flash("You have successfully logged out! Thanks for visiting.", category="info")
    return redirect(url_for("home_page"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
