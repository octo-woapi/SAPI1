#!/usr/bin/python
# coding=utf-8

from flask import Flask, jsonify, url_for
from flask_cors import CORS
from models import db, User
from json_encoder import SapiJSONEncoder
from routing import routing


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

# init database model
db.app = app
db.init_app(app)
db.create_all()


# ************** MODELS INITIALIZATION ***************

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)

# this line should be the last in order to insert all tuples
db.session.commit()


# ********************* ROUTING *********************

app.register_blueprint(routing, url_prefix='/sapi/')

