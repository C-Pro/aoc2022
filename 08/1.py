import re
from collections import deque


def getints(line):
    return [int(s) for s in list(line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = [getints(l) for l in lines]


def visR(a, r, c):
    be = True
    af = True
    for i in range(0, c):
        if a[r][i] >= a[r][c]:
            be = False
    for i in range(c+1, len(a[r])):
        if a[r][i] >= a[r][c]:
            af = False

    return be or af


def visC(a, r, c):
    be = True
    af = True
    for i in range(0, r):
        if a[i][c] >= a[r][c]:
            be = False
    for i in range(r+1, len(a)):
        if a[i][c] >= a[r][c]:
            af = False

    return be or af


cnt = len(a)*2 + len(a[0])*2 - 4
for r in range(1, len(a)-1):
    for c in range(1, len(a[0])-1):
        if visC(a, r, c) or visR(a, r, c):
            #print(f"({r},{c}) = {a[r][c]}")
            cnt += 1

print(cnt)
