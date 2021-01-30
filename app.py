import requests
import json

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
    
app = Flask(__name__)
api = Api(app)

date = input("Insert date (YYYY-MM-DD): ")
origin = input("Origin Location (Ex. DFW): ")
dest = input("Insert Desination (Ex. ORD): ")

data = requests.get(f"http://amai-test.herokuapp.com/flights?date={date}&origin={origin}&destination={dest}")
res = json.loads(data.text)

print(res)


