#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    with open(filename, 'a') as file:
        a = file.write(text)
        return(a)
        print(len(text))
