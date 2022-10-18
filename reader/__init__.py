# __init__ file
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

# Folder for static picture
UPLOAD_FOLDER = 'uploads'

# app initialization 
app = Flask(__name__)

# configs bd this app
basedir = os.path.abspath(os.path.dirname(__file__))
# 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Dan1lka2@22'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# bd initialization
db = SQLAlchemy(app)

from reader import routes, models

