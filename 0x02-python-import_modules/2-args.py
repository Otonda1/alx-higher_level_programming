#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    suffix = 's'
    separator = ':'

    if n == 0:
        separator = '.'

    if n == 1:
        suffix = ''

    print("{} argument{}{}".format(n, suffix, separator))
    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))
