import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


with open("test.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = [getints(l) for l in lines]

print(a)
