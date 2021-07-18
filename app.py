from flask_pymongo import PyMongo
from flask import Flask, request, jsonify
from flask_cors import CORS


from gg_search import pipeline_gg_search

import random
from datetime import datetime,timezone
import time
import os
import time
from dotenv import load_dotenv

load_dotenv()
# from mongoengine import connect

app = Flask(__name__)


api_key = os.getenv('GG_API')
cse_id = os.getenv('CUSTOM_SEARCH_ID')


# khoi tao app
app = Flask(__name__)
CORS(app)


def msg(code, mess=None):
    if code == 200 and mess is None:
        return jsonify({"code": 200, "value": True})
    else:
        return jsonify({"code": code, "message": mess}), code

def get_new_id():
    while (True):
        _id = str(random.randint(100000, 999999))
        if _id not in StateTracker_Container.keys():
            return _id
@app.route('/api/gg-search', methods=['POST'])
def post_api_cse_assistant():
    input_data = request.json
    data = input_data['data']
    print(input_data['data'])
    result = pipeline_gg_search(data,api_key,cse_id)
    return result

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0',port=6969,debug=True)