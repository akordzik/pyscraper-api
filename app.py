import os
import json

from bson import json_util
from flask import Flask
from flask import request

from src.mongo_handler import MongoHandler
from src.auth import CustomAuth

app = Flask(__name__)
app.config['BASIC_AUTH_FORCE'] = True

mongo_handler = MongoHandler(os.environ['MONGOLAB_URI'])
basic_auth = CustomAuth(app, os.environ['USERNAME'], os.environ['PASSWORD'])


@app.route('/adverts/')
def get():
    adverts = mongo_handler.get_adverts(request.authorization.username)
    return json.dumps(adverts, default=json_util.default, ensure_ascii=False).encode('utf8')
