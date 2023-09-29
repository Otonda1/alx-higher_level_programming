#!/usr/bin/python3
"""
Sends request to URL, displays body of response,
catches errors
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
