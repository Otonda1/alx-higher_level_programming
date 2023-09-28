#!/bin/bash
# Send POST request to given URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
