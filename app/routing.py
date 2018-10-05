#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from models import Pet, User, Client, Mission, Candidate
from models import db

routing = Blueprint('routing', __name__)


# ********************** ROUTES **********************

@routing.route("hello", strict_slashes=False)
def say_hello():
    return jsonify("Hello SAPI1")

@routing.route("users", strict_slashes=False)
def get_all_users():
    return jsonify(User.query.all())

@routing.route("clients")
def get_clients():
    return jsonify(Client.query.all())

@routing.route("clients/<int:id>/missions")
def get_client_missions(id):
    client = Client.query.get(id)
    return jsonify(client.missions)

@routing.route("clients/<int:client_id>/missions/<int:mission_id>", methods=['GET'])
def get_mission(client_id, mission_id):
    client = Client.query.get(client_id)
    mission = Mission.query.get(mission_id)
    # TODO verifier la cohérence dans la requete
    return jsonify(mission)

@routing.route("clients/<int:client_id>/missions", methods=['POST'])
def create_mission(client_id):
    client = Client.query.get(client_id)

    body = request.get_json()
    new_mission = Mission(job_title=body["title"], slots=body["slots"], start_date=body["date"])
    client.missions.append(new_mission)
    db.session.commit()

    return jsonify(new_mission), 201

@routing.route("clients/<int:client_id>/missions/<int:mission_id>", methods=['PATCH'])
def modify_mission(client_id, mission_id):

    body = request.get_json()
    ze_candidate = Candidate.query.get(body["candidate_id"])
    mission = Mission.query.get(mission_id)
    ze_candidate.mission_id = mission_id

    db.session.commit()

    return jsonify(mission)