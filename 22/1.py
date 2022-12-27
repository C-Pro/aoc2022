import re
from collections import deque

m = {}
W = 0
H = 0

start = None

with open("input.txt", "rt") as fi:
    parts = fi.read().split("\n\n")
    H = len(parts[0].splitlines())
    for r, line in enumerate(parts[0].splitlines()):
        for c, v in enumerate(line):
            if v in ('.', '#'):
                if start == None and v == '.':
                    start = c
                m[(r, c)] = v
                if c + 1 > W:
                    W = c + 1

rules = parts[1].strip()

# print(rules)
# print(m)


def draw():
    for r in range(H):
        for c in range(W):
            if (r, c) not in m:
                print(" ", end="")
            else:
                print(m[(r, c)], end="")
        print()
    print("-"*W)


def getStep(r):
    if r[0].isalpha():
        return (r[0], r[1:])
    i = 0
    s = ""
    while i < len(r) and r[i].isnumeric():
        s += r[i]
        i += 1
    return (int(s), r[i:])


r = 0
c = start
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirsym = [">", "v", "<", "^"]
dir = dirs[0]


def move(r, c, dir, n):
    if dir[0] != 0:
        nr = r
        pr = r
        while n > 0:
            xr = (nr + dir[0]) % H
            if (xr, c) not in m:
                nr = xr
                continue
            if m[(xr, c)] == "#":
                return (pr, c)
            nr = xr
            pr = nr
            if m[(nr, c)] in (".", "<", "^", "v", ">"):
                n -= 1
                m[(nr, c)] = dirsym[dirs.index(dir)]
                continue
        return (nr, c)
    if dir[1] != 0:
        nc = c
        pc = c
        while n > 0:
            xc = (nc + dir[1]) % W
            if (r, xc) not in m:
                nc = xc
                continue
            if m[(r, xc)] == "#":
                return (r, pc)
            nc = xc
            pc = nc
            if m[(r, nc)] in (".", "<", "^", "v", ">"):
                n -= 1
                m[(r, nc)] = dirsym[dirs.index(dir)]
                continue
        return (r, nc)


while rules != "":
    cmd, rules = getStep(rules)
    if type(cmd) == str:
        if cmd == "R":
            dir = dirs[(dirs.index(dir) + 1) % 4]
        else:
            dir = dirs[(dirs.index(dir) - 1) % 4]
        continue

    r, c = move(r, c, dir, cmd)
    #print(cmd, r, c, dirs.index(dir))
    # draw()

print((r+1)*1000 + (c+1) * 4 + dirs.index(dir))
