#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        n = 0
    elif i % 2 != 0:
        n = 32
    print("{}".format(chr(i - n)), end="")
