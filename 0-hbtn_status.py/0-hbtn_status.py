#!/usr/bin/python3
"""
sends GET request to https://alx-intranet.hbtn.io/status
"""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        utf8_content = body.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(utf8_content))
