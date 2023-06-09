#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num = len(sys.argv) - 1
    total = 0
    if num < 1:
        print("0")
    elif num > 1:
        for i in range(1, num + 1):
            total += int(sys.argv[i])
        print("{}".format(total))
