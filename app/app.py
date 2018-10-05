#!/usr/bin/python
# coding=utf-8

from flask import Flask, jsonify, url_for
from flask_cors import CORS
from models import db, User, Client, Mission, Candidate
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

chronopost = Client(name='chronopost', siret='234535645')
coca = Client(name='cocacolacompany', siret='23453545444')
pole_emploi = Client(name='poleemploi', siret='42')

mission1 = Mission(job_title='livreur', slots='10', start_date='01/01/2020')

toto = Candidate(name='Toto', email='toto@gmail.com')
titi = Candidate(name='Titi', email='titi@gmail.com')

mission1.candidates.append(toto)
chronopost.missions.append(mission1)

db.session.add(chronopost)
db.session.add(coca)
db.session.add(pole_emploi)
db.session.add(titi)

# this line should be the last in order to insert all tuples
db.session.commit()


# ********************* ROUTING *********************

app.register_blueprint(routing, url_prefix='/sapi/')

@app.errorhandler(KeyError)
def baaaaad(error):
    return jsonify("Le champ "+str(error.args[0])+" est obligatoire"), 400

