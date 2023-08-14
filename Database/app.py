from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func


import os
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)
api = Api(app)

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

# Import models
import models.post,models.comment,models.community,models.upvote,models.downvote

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5000, debug=True)