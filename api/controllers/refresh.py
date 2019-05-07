#!/usr/bin/env python3
# coding: utf8

"""
Dummy controller to test REST requests.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask_restful import Resource

from context import Context


class RefreshController(Resource):

    def get(self):
        Context.reresh()
        return True, 200

    def post(self):
        Context.reresh()
        return True, 200