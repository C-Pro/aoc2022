import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()


x = 1
cycle = 1

for line in lines:

    if line[:4] == "noop":
        if ((cycle-1) % 40) >= x-1 and (cycle-1) % 40 <= x+1:
            print("#", end="")
        else:
            print(".", end="")
        cycle += 1
        if (cycle-1) % 40 == 0:
            print()
        continue

    val = getints(line)[0]
    for i in range(2):
        if ((cycle-1) % 40) >= x-1 and ((cycle-1) % 40) <= x+1:
            print("#", end="")
        else:
            print(".", end="")
        cycle += 1
        if (cycle-1) % 40 == 0:
            print()
    x += val
