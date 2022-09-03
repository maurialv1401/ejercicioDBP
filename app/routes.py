from app import app
import re
from flask import render_template, request
from app import db
from app.models import NewUser
import requests
import json

@app.route("/")
def index():
    u1 = NewUser(username="...", email="...", password="...")
    return render_template("index.html")
