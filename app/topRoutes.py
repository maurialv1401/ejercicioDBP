from app import app
import re
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser
import requests
import json

@app.route("/")
@app.route("/index")
def index():
    u1 = NewUser(username="...", email="...", password="...")
    return render_template("index.html")
@app.route("/users")
def getUsers():
    users = NewUser.query.all()
    userString = ""
    for user in users:
        userString += user.username + " " + user.password + " " + user.email + "<br>"
    return userString