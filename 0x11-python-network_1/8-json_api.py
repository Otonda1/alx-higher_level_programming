#!/usr/bin/python3
"""
Sends POST request to given url and searches for letter
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data={'q': q})
    if res.headers.get('content-type') == 'application/json':
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    else:
        print("Not a valid JSON")
