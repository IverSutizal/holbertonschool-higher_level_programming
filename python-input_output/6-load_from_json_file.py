#!/usr/bin/python3
"""Create object from aa JSON file"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”
    """
    with open(filename) as file:
        d = json.load(file)
        return(d)
