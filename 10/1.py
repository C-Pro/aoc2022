import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

x = 1
cycle = 1
s = 0
for line in lines:
    if line[:4] == "noop":
        if cycle in [20, 60, 100, 140, 180, 220]:
            s += x*cycle
        cycle += 1
        continue

    val = getints(line)[0]
    for i in range(2):
        if cycle in [20, 60, 100, 140, 180, 220]:
            s += x*cycle
        cycle += 1
    x += val

print(s)
