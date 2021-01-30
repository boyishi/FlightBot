import requests
import json

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

print("hello world")

app = Flask(__name__)
api = Api(app)

data = requests.get('http://amai-test.herokuapp.com/flights?date=2020-01-01')
converted = json.loads(data.text)
print(converted[0])