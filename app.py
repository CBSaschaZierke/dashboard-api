import flask
from bson import json_util
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from flask_cors import CORS
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
CORS(app)
mongo = PyMongo(app)


@app.route('/')
def home():
    return


@app.route('/residential', methods=['GET'])
def find_residential():  # put application's code here
    test = mongo.db.acs.find_one({"name": "Residential"})
    response = flask.jsonify(parse_json(test))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/commercial', methods=['GET'])
def find_commercial():  # put application's code here
    test = mongo.db.acs.find_one({"name": "Commercial"})
    response = flask.jsonify(parse_json(test))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/healthcare', methods=['GET'])
def find_health_care():  # put application's code here
    test = mongo.db.acs.find_one({"name": "Health Care"})
    response = flask.jsonify(parse_json(test))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.debug = True
    app.run()


def parse_json(data):
    return json.loads(json_util.dumps(data))
