#!/usr/bin/python
# coding=utf-8

from flask.json import JSONEncoder
from flask import url_for
from models import User, Pet, Client, Mission, Candidate

class SapiJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return{
                'username':obj.username,
                'email':obj.email
            }
        if isinstance(obj, Client):
            return{
                'name':obj.name,
                'siret':obj.siret,
                'missions':obj.missions
            }
        if isinstance(obj, Mission):
            return{
                'job_title':obj.job_title,
                #'client_name':obj.client.name,
                #'client':obj.client,
                'slots':obj.slots,
                'link':url_for('routing.get_mission', client_id=obj.client_id, mission_id=obj.id, _external=True),
                'candidates':obj.candidates
            }
        if isinstance(obj, Candidate):
            return{
                'name':obj.name
            }

        return super(SapiJSONEncoder, self).default(obj)
