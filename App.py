#!/usr/bin/env python
from flask_sqlalchemy import SQLAlchemy
from HelpdeskModels import *
from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sudhanshu@localhost:3306/helpdesk_prod'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])