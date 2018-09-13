#!/usr/bin/python
# coding=utf-8

from flask import Flask, jsonify, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask.json import JSONEncoder


# ********************** UTILS ***********************

class SapiJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return{
                'username':obj.username,
                'email':obj.email
            }

        return super(SapiJSONEncoder, self).default(obj)


# ********************** CONFIG **********************

# create the application
app = Flask("sapi1")

# CORS handling
CORS(app, resources={r"/*": {"origins": "*"}})

# custom jsonEncoder
app.json_encoder = SapiJSONEncoder

# database connexion
database_url = 'sqlite://'  # this is a local in-memory database for testing purpose only
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning
db = SQLAlchemy(app)


# **************** MODELS DEFINITION *****************

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# this line should be the last in order to create all models
db.create_all()


# ************** MODELS INITIALIZATION ***************

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)

# this line should be the last in order to insert all tuples
db.session.commit()


# ********************** ROUTES **********************

@app.route("/sapi/hello", strict_slashes=False)
def say_hello():
    return jsonify("Hello SAPI1")

@app.route("/sapi/users", strict_slashes=False)
def get_all_users():
    return jsonify(User.query.all())

