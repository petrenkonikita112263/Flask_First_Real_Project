from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "717d3b62413d3ef9eb728196"
app_db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_mamanger = LoginManager(app)
login_mamanger.login_view = "log_in_page"

from market import routes
