#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pets = db.relationship('Pet', backref='owner', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return '<Pet %r>' % self.pet_name

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    siret = db.Column(db.String(80), unique=True, nullable=True)
    missions = db.relationship('Mission', backref='client', lazy=True)

    def __repr__(self):
        return '<Client %r>' % self.name

class Mission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(80), unique=False, nullable=False)
    slots = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.String(80), unique=False, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    candidates = db.relationship('Candidate', backref='mission', lazy=True)

    def __repr__(self):
        return '<Mission %r>' % self.job_title

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mission_id = db.Column(db.Integer, db.ForeignKey('mission.id'), nullable=True)

    def __repr__(self):
        return '<Candidate %r>' % self.name