import re
from collections import deque

m = {}

start = None

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for r, line in enumerate(lines):
        for c, v in enumerate(line):
            if v == '#':
                m[(r, c)] = v


def mm():
    return (min([r for r, _ in m.keys()]),
            max([r for r, _ in m.keys()]),
            min([c for _, c in m.keys()]),
            max([c for _, c in m.keys()]),
            )


def draw():
    (sr, er, sc, ec) = mm()
    for r in range(sr-1, er+2):
        for c in range(sc-1, ec+2):
            if (r, c) not in m:
                print(".", end="")
            else:
                print(m[(r, c)], end="")
        print()
    print("-"*(ec-sc+3))


# draw()


moves = [((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
         ((1, 0), [(1, -1), (1, 0), (1, 1)]),
         ((0, -1), [(-1, -1), (0, -1), (1, -1)]),
         ((0, 1), [(-1, 1), (0, 1), (1, 1)]),
         ]


def occ(c, d):
    return (c[0]+d[0], c[1]+d[1]) in m


def lone(c):
    for _, chks in moves:
        for chk in chks:
            if occ(c, chk):
                return False
    return True


for i in range(123490812390481290384903):
    props = {}
    for c, v in m.items():
        if lone(c):
            continue
        j = i % 4
        k = 0
        for k in range(4):
            off, chks = moves[j]
            good = True
            for chk in chks:
                if occ(c, chk):
                    good = False
            if good:
                cn = (c[0]+off[0], c[1]+off[1])
                prop = props.get(cn)
                if prop is None:
                    prop = (c, 0)
                else:
                    prop = (prop[0], prop[1] + 1)
                props[cn] = prop
                break
            j = (j + 1) % 4
    moved = False
    for c, p in props.items():
        if p[1] == 0:
            moved = True
            del (m[p[0]])
            m[c] = "#"
    if not moved:
        print(i+1)
        exit()
    # draw()

(sr, er, sc, ec) = mm()
total = (er-sr+1) * (ec - sc+1)
print(total - len(m))
