import os
import jwt

from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, jsonify

# from db.main import Database
# from db.tables import User_, Post_
# from dev.exceptions import *
# from dev.utils import *

app = Flask(__name__)


if os.environ.get('DOCKERIZED', '') != 'true':
    from dotenv import load_dotenv
    load_dotenv()


DATABASE_URL = os.getenv('POSTGRES_CONN')
# JWT_SECRET_TOKEN = os.getenv('JWT_SECRET_TOKEN')
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
# db = Database(Session, engine)
# db.create()


def get_data():
    ...


@app.route('/api/projects', methods=['GET'])
def projects():
    ...


@app.route('/api/olympiads', methods=['GET'])
def olympiads():
    ...


@app.route('/api/skills', methods=['GET'])
def skills():
    ...


if __name__ == "__main__":
    app.run(debug=True, port=8080)
