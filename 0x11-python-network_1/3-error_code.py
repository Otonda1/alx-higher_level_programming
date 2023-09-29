#!/usr/bin/python3
"""
Sends request to URL, displays body of response,
catches errors
"""

import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
