import re
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


minX = math.inf
maxX = -math.inf
minY = math.inf
maxY = -math.inf
for row in a:
    s = row[:2]
    b = row[2:]
    d = md(s,b)
    left = s[0] - d
    if left < minX:
        minX = left
    right = s[0] + d
    if right > maxX:
        maxX = right
    top = s[1] - d
    if top < minY:
        minY = top
    bot = s[1] + d
    if bot > maxY:
        maxY = bot

cnt = 0
for x in range(minX, maxX+1):
    y = 2000000
    can = True
    for row in a:
        s = md(row[:2], row[2:])
        if md([x, y], row[:2]) <= s:
            can = False
            break
    if not can:
        cnt += 1
b2 = len(set([(r[2], r[3]) for r in a if r[3] == 2000000]))
print(b2)
print(cnt-b2)
