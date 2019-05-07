#!/usr/bin/env python3
# coding: utf8

"""
unmix.io board RESTful API to receive information adn overview over unmix-net training runs.
"""


__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import os

from controllers.dummy import DummyController
from controllers.runs import RunsController
from controllers.refresh import RefreshController
from context import Context


def register_controllers(api):
    api.add_resource(DummyController, '/dummy/<string:name>')
    api.add_resource(RunsController, '/runs')
    api.add_resource(RefreshController, '/refresh')

def app():
    app = Flask(__name__)
    api = Api(app)
    register_controllers(api)
    CORS(app, resources={"*": {"origins": "*"}})
    Context.initialize()
    app.run('0.0.0.0', port=os.environ['UNMIX_BOARD_API_PORT'])


if __name__ == "__main__":
    app()