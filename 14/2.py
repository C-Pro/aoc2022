import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


def draw(m):
    minX = 99999999
    maxX = -9999999
    minY = 99999999
    maxY = -9999999
    for p in m.keys():
        if p[0] < minX:
            minX = p[0]
        if p[0] > maxX:
            maxX = p[0]
        if p[1] < minY:
            minY = p[1]
        if p[1] > maxY:
            maxY = p[1]

    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            v = m.get((x, y))
            if v:
                print(v, end="")
            else:
                print(".", end="")
        print()

    print()

    return maxY


m = {}

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for line in lines:
        pts = line.split("->")
        pp = None
        for p in [getints(x) for x in pts]:
            if pp is not None:

                if pp[0] != p[0]:
                    for x in range(min(pp[0], p[0]), max(pp[0], p[0])+1):
                        m[(x, p[1])] = "#"
                elif pp[1] != p[1]:
                    for y in range(min(pp[1], p[1]), max(pp[1], p[1])+1):
                        m[(p[0], y)] = "#"

            pp = p

maxY = draw(m)


def free(m, p):
    return p not in m.keys()


def drop(m):
    grain = (500, 0)
    while True:
        if grain[1] > maxY:
            m[grain] = "@"
            return True
        if free(m, (grain[0], grain[1]+1)):
            grain = (grain[0], grain[1]+1)
        elif free(m, (grain[0]-1, grain[1]+1)):
            grain = (grain[0]-1, grain[1]+1)
        elif free(m, (grain[0]+1, grain[1]+1)):
            grain = (grain[0]+1, grain[1]+1)
        else:
            m[grain] = "@"
            if grain == (500, 0):
                return False
            return True


cnt = 0
while drop(m):
    cnt += 1

print(cnt+1)
