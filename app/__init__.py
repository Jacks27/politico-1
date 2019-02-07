from flask import Flask
from flask import Blueprint
from app.api.v1.views.party_view import my_v1 as v1



def create_app():
    app = Flask(__name__)

    app.register_blueprint(v1)
    return app