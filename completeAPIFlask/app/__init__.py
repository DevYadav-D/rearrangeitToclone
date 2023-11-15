from flask import Flask
from sqlalchemy import sql


app = Flask(__name__)

@app.route('/')
def mainpage():
    return "decent manner to write applicaiton"

# from app import routes
# from app import models