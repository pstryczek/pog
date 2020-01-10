from db import db
from default_config import Config
from flask import Flask

from pymongo import MongoClient

test = Flask(__name__)
test.config.from_object(Config)

myclient = MongoClient("mongodb://localhost:27017/UTA_Enrollment")
mydb = myclient["UTA_Enrollment"]
mycol = mydb["flashes"]


for x in mycol.find():
  print(x)