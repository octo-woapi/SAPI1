#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from models import Pet, User

routing = Blueprint('routing', __name__)


# ********************** ROUTES **********************

@routing.route("hello", strict_slashes=False)
def say_hello():
    return jsonify("Hello SAPI1")

@routing.route("users", strict_slashes=False)
def get_all_users():
    return jsonify(User.query.all())

