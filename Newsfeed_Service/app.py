from flask import Flask,request,jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func
from flask_cors import CORS

import datetime

import os
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app,origins = 'http://localhost:8000')

# Load environment variables
load_dotenv()
db_url = os.getenv('DATABASE_URL')

# Connect to database
conn = psycopg2.connect(db_url, sslmode='prefer')

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)



migrate = Migrate(app, db)

from router import api

import models  #importing this the running program will know all the model classes(or the tables of database) 


if __name__ == '__main__':
    app.run(port=5000, debug=True)



