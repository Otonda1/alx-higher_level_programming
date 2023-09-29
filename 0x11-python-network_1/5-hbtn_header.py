#!/usr/bin/python3
"""
Takes in URL, sends request to it and displays
the value of the X-Request-Id header variable
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as res:
        print(res.headers.get("X-Request-Id"))
