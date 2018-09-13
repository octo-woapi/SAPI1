#!/usr/bin/python
# coding=utf-8

from flask.json import JSONEncoder
from models import User, Pet

class SapiJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return{
                'username':obj.username,
                'email':obj.email
            }

        return super(SapiJSONEncoder, self).default(obj)
