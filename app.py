from flask import Flask
from flask_restful import Api
from db import db
from ma import ma
from default_config import Config
from resources.flashes import Flashes,FlashesList

from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv(".env", verbose=True)

app.config.from_object(Config)

# app.config.from_object("default_config")  # load default configs from default_config.py
# app.config.from_envvar(
#     "APPLICATION_SETTINGS"
# )

api = Api(app)

# @app.before_first_request
# def create_tables():
#         db.create_all()

api.add_resource(Flashes, "/flash/<string:flash_id>")
api.add_resource(FlashesList, "/flashes")

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=7000, debug=True)