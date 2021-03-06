import flask
from bson import json_util
from flask import Flask, send_file
from flask_pymongo import PyMongo
from flask_cors import CORS
import json

app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://194.163.147.192:27017/test"
app.config["MONGO_URI"] = "mongodb://192.168.178.28:27017/test"
CORS(app)
mongo = PyMongo(app)


def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.route('/')
def home():
    return 'Hello'


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


@app.route('/germany', methods=['GET'])
def find_germany():
    test = mongo.db.germanies.find_one()
    response = flask.jsonify(parse_json(test))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/germany/objects', methods=['GET'])
def find_germany_objects():
    test = mongo.db.germanies.find_one()
    response = flask.jsonify(parse_json(test['objects']))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/germany/states', methods=['GET'])
def find_germany_states():
    db_data = mongo.db.germanies.find_one()
    response = flask.jsonify(parse_json(db_data['state']))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", debug=True)
