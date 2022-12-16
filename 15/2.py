import math
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
a = [getints(l) for l in lines]


def md(a, b):
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    return x+y


for y in range(0, 4000001):
    x = 0
    while x <= 4000000:
        can = True
        for row in a:
            s = md(row[:2], row[2:])
            d = md([x, y], row[:2])
            if d <= s:
                x += s-d + 1
                can = False
                break
        if can:
            print(x*4000000 + y)
            exit()
        else:
            if y % 100000 == 0:
                print(f"{y/4000000*100}%")
