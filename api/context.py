#!/usr/bin/env python3
# coding: utf8

"""
Context object of the api, initialized at startup.
"""


__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


import os
import glob

from models.run import Run


class Context(object):

    @staticmethod
    def initialize():
        Context.base_paths = os.environ['UNMIX_BOARD_API_PATHS'].split(";")
        Context.runs = []
        for path in Context.base_paths:
            Context.runs += Context.__search_runs(path)

    @staticmethod
    def __search_runs(path):
        runs = []
        print("Search runs in folder: %s." % path)
        for file in glob.iglob(os.path.join(path, '**', 'configuration.jsonc'), recursive=False):
            runs.append(Run(os.path.dirname(file)))
        return runs

    @staticmethod
    def refresh():
        Context.initialize()
