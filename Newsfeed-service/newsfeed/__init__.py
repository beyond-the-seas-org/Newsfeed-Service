from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2, dotenv, os
from flask_restx import Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app,origins = 'http://localhost:3000')


dotenv.load_dotenv()
db_url = os.getenv('DATABASE_URL')

conn = psycopg2.connect(db_url, sslmode='prefer')

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from newsfeed.routes import *