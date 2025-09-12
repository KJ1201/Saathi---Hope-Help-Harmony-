from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    phone_no = db.Column(db.String(150))
    role = db.Column(db.String(150))
    institue = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())