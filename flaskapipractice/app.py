import os
import pymysql
from http import HTTPStatus
from flask_cors import CORS
from flask import Flask, redirect, request, jsonify, url_for, abort
from db import Database
from config import DevelopmentConfig as devconf

host = os.environ.get('FLASK_SERVER_HOST', devconf.HOST)
port = os.environ.get('FLASK_SERVER_PORT', devconf.PORT)
version = str(devconf.VERSION).lower()
url_prefix = str(devconf.URL_PREFIX).lower()
route_prefix = f"/{url_prefix}/{version}"

def createapp():
    app = Flask(__name__)
    cors = CORS(app, resources={f"{route_prefix}/*": {"origins": "*"}})
    app.config.from_object(devconf)
    return app

def get_response_msg(data, status_code):
    message = {
        'status': status_code,
        'data': data if data else 'No records found'
    }
    response_msg = jsonify(message)
    response_msg.status_code = status_code
    return response_msg

app = createapp()
wsgi_app = app.wsgi_app
db = Database(devconf)


## /api/v1/getname ? test1
@app.route(f"{route_prefix}/getname", methods=['GET'])
def getdata():
    try:
        empName = request.args.get('name', default='test2', type=str)
        query = f"SELECT * FROM emp.testemp WHERE name='{empName.upper()}'"
        records = db.run_query(query=query)
        response = get_response_msg(records, HTTPStatus.OK)
        db.close_connection()
        return response
    except pymysql.MySQLError as sqle:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(sqle))
    except Exception as e:
        abort(HTTPStatus.BAD_REQUEST, description=str(e))

@app.route('/', methods=['GET'])
def home():
    cur = pymysql.connect(user='user', passwd='password')
    cur =cur.cursor()
    data = cur.fetchall()
    cur.close()
    return ("let's the game begin \n",jsonify(data))

@app.route('/create/', methods =['POST'])
def create_post():
    req_data = request.get_json()
    new_emp = {
        'id':req_data['id'],
        'name':[]
    }  

    return jsonify(req_data)   
# Launch the application
if __name__ == "__main__":
    app.run(host=host, port=port)