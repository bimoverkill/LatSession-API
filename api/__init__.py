from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

app = FlaskAPI(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://developer:Developer12345@localhost/toko_online"

db = SQLAlchemy(app)

from . import route