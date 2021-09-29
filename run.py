# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from flask import Flask, redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
from decouple import config

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY", "9a7sam_jaksjda")

app.config["GITHUB_OAUTH_CLIENT_ID"]     = config('GITHUB_OAUTH_CLIENT_ID')
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = config('GITHUB_OAUTH_CLIENT_SECRET')

github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")

@app.route("/")
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok
    return "You are @{login} on GitHub".format(login=resp.json()["login"])

