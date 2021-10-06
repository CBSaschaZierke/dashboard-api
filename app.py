from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)


@app.route('/')
def hello_world():  # put application's code here
    test = mongo.db.acs.find_one({"name": "Residential"})
    print(test)
    return dumps(test)


@app.route('/commercial')
def find_commercial():  # put application's code here
    test = mongo.db.acs.find_one({"name": "Commercial"})
    print(test)
    return dumps(test)


@app.route('/healthcare')
def find_health_care():  # put application's code here
    test = mongo.db.acs.find_one({"name": "Health Care"})
    print(test)
    return dumps(test)


if __name__ == '__main__':
    app.debug = True
    app.run()
