# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from flask import Flask, redirect, url_for
from flask import render_template, request, url_for, redirect

from flask_dance.contrib.github import make_github_blueprint, github
from decouple import config

# Construct the Flask APP
app = Flask(__name__)

# Inject the Configuration (loaded from .env)
app.config.from_object('app.config.Config')

# Register the Github OAuth BP built by Flask-Dance 
github_bp = make_github_blueprint()
app.register_blueprint(github_bp, url_prefix="/login")

# Define the main route
@app.route("/")
def index():

    github_id=None

    if github.authorized:
        
        # all available data: https://docs.github.com/en/rest/reference/users 
        resp = github.get("/user")    
        assert resp.ok
        github_id=resp.json()["login"]

    return render_template( 'index.html', github=github, github_id=github_id )
