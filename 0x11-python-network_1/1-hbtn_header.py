#!/usr/bin/python3
"""
     a Python script that takes in a URL, sends a request 
     to the URL and displays the value of the X-Request-Id
"""
from urllib import request
from sys import argv
if __name__ == "__main__":
    with request.urlopen(argv[1]) as re:
        for key, value in re.headers.items():
            if key == 'X-Request-Id':
                print(value)
        
