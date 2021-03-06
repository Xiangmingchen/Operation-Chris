from project import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from passlib.hash import pbkdf2_sha256 as passhash

class Order(db.Model):

    __tablename__= "orders"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    patty = db.Column(db.Integer)
    no_bun = db.Column(db.Boolean)
    cheese = db.Column(db.Boolean)
    bacon = db.Column(db.Boolean)
    addons = db.Column(db.String,nullable=True)
    recipient_id = db.Column(db.Integer,ForeignKey('users.id'))

    def __repr__(self):
        return '<name {}>'.format(self.name)


class User(db.Model):

    __tablename__="users"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    meals = db.Column(db.Integer,nullable=False)

    password = db.Column(db.String,nullable=False)
    orders = relationship("Order", backref="recipient", cascade='save-update, merge, delete')


    def __init__(self,name,email,meals,password):
        self.name=name
        self.email=email
        self.meals=meals
        self.password=passhash.encrypt(password,rounds=20000,salt_size=16)

    def validate_password(self,password):
        return passhash.verify(password,self.password)

    def __repr__(self):
        return '<{}-{}>'.format(self.name,self.email)
