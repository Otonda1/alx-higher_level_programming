#!/bin/bash
# Takes in a URL, sends a request to it, returns length of response
curl -s "$1" | wc -c
