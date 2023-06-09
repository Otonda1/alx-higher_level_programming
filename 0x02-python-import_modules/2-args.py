#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = len(sys.argv) - 1
    period = ':'
    suffix = 's'

    if num == 0:
        period = ''
    if num == 1:
        suffix = ''
    print("{} argument{}{}".format(num, suffix, period))
    for i in range(1, num +1):
        print("{}: {}".format(i, sys.argv[i]))
