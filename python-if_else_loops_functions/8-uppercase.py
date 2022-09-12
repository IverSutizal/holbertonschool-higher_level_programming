#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            upper = ord(i) - 32
        else:
            upper = ord(i)
        print("{:s}".format(chr(upper)), end="")
    print("")
