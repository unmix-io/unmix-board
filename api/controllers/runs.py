#!/usr/bin/env python3
# coding: utf8

"""
Returns all runs and overview information.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


from flask_restful import Resource

from context import Context


class RunsController(Resource):

    def get(self):
        return [run.serialize() for run in Context.runs], 200