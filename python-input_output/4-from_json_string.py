#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure)
    represented by a JSON string
    """
    datastore = json.loads(my_str)
    return(datastore)
