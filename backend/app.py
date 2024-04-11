import os
# import jwt

from functools import wraps
from cachetools import TTLCache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, request, jsonify

# from ..db.main import Database
from db.main import Database
# from db.tables import User_, Post_
# from dev.exceptions import *
# from dev.utils import *

app = Flask(__name__)


if os.environ.get('DOCKERIZED', '') != 'true':
    from dotenv import load_dotenv
    load_dotenv()


DATABASE_URL = os.getenv('POSTGRES_CONN')
# JWT_SECRET_TOKEN = os.getenv('JWT_SECRET_TOKEN')
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
db = Database(Session, engine)
db.create()
# print(db.projects.get_all())


def setup() -> None:
    db.create()


def get_data() -> dict:
    data = {}
    data['projects'] = db.projects.get_all()
    data['events'] = db.events.get_all()
    data['skills'] = db.skills.get_all()
    # print(data)
    return data


@app.route("/")
def main():
    return "ok"


@app.route('/api/projects', methods=['GET'])
def projects():
    data = get_data()
    print(data)
    return jsonify({'ok': '<3'}), 200


@app.route('/api/olympiads', methods=['GET'])
def olympiads():
    ...


@app.route('/api/skills', methods=['GET'])
def skills():
    ...


if __name__ == "__main__":
    setup()
    # get_data()
    app.run(debug=True, port=8080)
