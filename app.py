import os
import json

from bson import json_util
from flask import Flask
from pymongo.mongo_client import MongoClient
from flask_basicauth import BasicAuth

app = Flask(__name__)

client = MongoClient(os.environ['MONGOLAB_URI'])
db = client.get_default_database()
collection = db['advertisements']


class CustomAuth(BasicAuth):
    def check_credentials(_, username: str, password: str):
        return username == os.environ['USERNAME'] and password == os.environ['PASSWORD']


app.config['BASIC_AUTH_FORCE'] = True
basic_auth = CustomAuth(app)


@app.route('/adverts/')
def get():
    adverts = list(collection.find())
    return json.dumps(adverts, default=json_util.default, ensure_ascii=False).encode('utf8')
