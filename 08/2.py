import re
from collections import deque


def getints(line):
    return [int(s) for s in list(line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = [getints(l) for l in lines]


def scoreIT(a, r, c):
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    for i in range(c-1, -1, -1):
        d1 += 1
        if a[r][i] >= a[r][c]:
            break
    for i in range(c+1, len(a[r])):
        d2 += 1
        if a[r][i] >= a[r][c]:
            break

    for i in range(r-1, -1, -1):
        d3 += 1
        if a[i][c] >= a[r][c]:
            break
    for i in range(r+1, len(a)):
        d4 += 1
        if a[i][c] >= a[r][c]:
            break

    return d1*d2*d3*d4

M = 0
for r in range(0, len(a)):
    for c in range(0, len(a[0])):
        sc = scoreIT(a, r, c)
        #print(f"({r},{c}) = {a[r][c]} == {sc}")
        if sc > M:
            M = sc

print(M)
