import re
from collections import deque

M = []
S = None
E = None


def h(c):
    return ord(c) - ord('a')


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for y, line in enumerate(lines):
        row = []
        for x, c in enumerate(list(line)):
            if c == "S":
                S = (x, y)
                row.append(h('a'))
                continue
            if c == "E":
                E = (x, y)
                row.append(h('z'))
                continue
            row.append(h(c))
        M.append(row)


#print(M, S, E)

curr = S
unvisited = set([])
paths = []
for y in range(len(M)):
    row = []
    for x in range(len(M[0])):
        unvisited.add((x, y))
        row.append(189374891234791238734981)
    paths.append(row)

paths[S[1]][S[0]] = 0
unvisited.remove((S[0], S[1]))


def H(coord):
    return M[coord[1]][coord[0]]


def V(coord):
    return paths[coord[1]][coord[0]]


def getMin():
    minV = 189374891234791238734981
    minI = 0
    l = list(unvisited)
    for i, coord in enumerate(l):
        if V(coord) < minV:
            minV = V(coord)
            minI = i
    if minV == 189374891234791238734981:
        raise ValueError("noway")
    return l[minI]


while len(unvisited) > 0:
    # print(curr)
    for next in [(curr[0]-1, curr[1]), (curr[0]+1, curr[1]), (curr[0], curr[1]-1), (curr[0], curr[1]+1)]:
        if next[0] < 0 or next[1] < 0:
            continue
        if next[0] > len(M[0]) - 1:
            continue
        if next[1] > len(M) - 1:
            continue
        if H(next) > H(curr) + 1:
            continue
        if next not in unvisited:
            continue
        v = V(curr) + 1  # H(next)
        if v < V(next):
            paths[next[1]][next[0]] = v
    if curr != S:
        unvisited.remove(curr)
    # if curr == E:
    #     break

    try:
        curr = getMin()
    except:
        break


print(paths[E[1]][E[0]])
