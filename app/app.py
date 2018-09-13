#!/usr/bin/python
# coding=utf-8

from flask import Flask, jsonify

app = Flask("sapi1")

@app.route("/sapi/hello", strict_slashes=False)
def say_hello():
    return jsonify("Hello SAPI1")