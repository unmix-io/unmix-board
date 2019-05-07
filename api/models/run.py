#!/usr/bin/env python3
# coding: utf8

"""
Response object for a training run.
"""

__author__ = 'David Flury, Andreas Kaufmann, Raphael Müller'
__email__ = "info@unmix.io"


import csv
import glob
import json
import os
import commentjson

class Run(object):

    def __init__(self, path):
        self.name = os.path.basename(path)
        self.path = path
        self.weights = [file for file in glob.iglob(os.path.join(path, 'weights', '*.h5'), recursive=True)]
        self.predictions = [file for file in glob.iglob(os.path.join(path, 'predictions', '*.wav'), recursive=True)]
        try:
            with open(os.path.join(path, "configuration.jsonc"), 'r') as file:
                self.configuration = commentjson.load(file)
        except:
            pass
        try:
            with open(os.path.join(path, "environment.json"), 'r') as file:
                self.environment = json.load(file)
        except:
            pass
        try:
            with open(os.path.join(path, "results.csv"), mode='r') as file:
                self.results = list(csv.DictReader(file, delimiter=';'))
        except:
            pass
        try:
            with open(os.path.join(path, "accuracy.csv"), mode='r') as file:
                self.accuracies = list(csv.DictReader(file, delimiter=';'))
        except:
            try: # Fallback for old filename
                with open(os.path.join(path, "accuracy_mix.csv"), mode='r') as file:
                    self.accuracies = list(csv.DictReader(file, delimiter=';'))
                pass
            except:
                pass

    def serialize(self):
        return self.__dict__
