with open("input.txt", "rt") as fi:
    wind = list(fi.read().strip())

figs = [
    """####""",
    """.#.
###
.#.""",
    """..#
..#
###""",
    """#
#
#
#""",
    """##
##""",
]

figz = [list(reversed(fig.splitlines())) for fig in figs]

m = {}


def draw(m, top=None, cnt=None):
    h = max(6, max([p[1] for p in m.keys()]))
    w = 7  # max([p[0] for p in m.keys()])
    if cnt is None:
        end = -1
        start = h
    else:
        end = top - cnt
        start = top
    for y in range(start, end, -1):
        print("|", end="")
        for x in range(w):
            if m.get((x, y)) == "#":
                print("#", end="")
            else:
                print(".", end="")
        print(f"|{y}", end="")
        print()
    for x in range(w+2):
        print("-" if cnt is None else "v", end="")
    print()


def put(f, x, y):
    global m
    mm = {}
    for yy, r in enumerate(f):
        for xx, c in enumerate(r):
            if c == "#":
                pos = (x+xx, y+yy)
                if pos[0] < 0 or pos[0] > 6:
                    return False
                if pos[1] < 0:
                    return False
                if m.get(pos) == "#":
                    return False
                mm[pos] = "#"
    for pos in mm:
        m[pos] = "#"
    # draw(m)
    return True


def erase(f, x, y):
    global m
    h = len(f)
    w = len(f[0])
    mm = {}
    for yy, r in enumerate(f):
        for xx, c in enumerate(r):
            if c == "#":
                pos = (x+xx, y+yy)
                if pos in m.keys():
                    del (m[pos])


def hash(m, top, n):
    h = 0
    for i, y in enumerate(range(top, top-n-1, -1)):
        for x in range(7):
            if m.get((x, y)) == "#":
                h += (7 ** i) * x
    return h


hashes = {}


def updHahses(h, n, top):
    global hashes
    v = hashes.get(h)
    if v is None:
        hashes[h] = [(n, top)]
        return False
    v.append((n, top))
    hashes[h] = v

    # at least 5 occurencies of pattern
    if len(v) < 5:
        return False
    dp0 = v[1][0] - v[0][0]
    dp1 = v[1][1] - v[0][1]
    # make sure occurencies are periodic
    for i in range(2, len(v)):
        d0 = v[i][0] - v[i-1][0]
        d1 = v[i][1] - v[i-1][1]
        if d0 != dp0:
            return False
        if d1 != dp1:
            return False
        dp0 = d0
        dp1 = d1
    print(f"HASH {h}", v)
    return True


top = 0
i = -1
n = -1
E = None
while E is None:
    n += 1
    f = figz[n % len(figz)]
    x = 2
    y = top + 3
    while True:
        i += 1
        erase(f, x, y)
        px = x
        w = wind[i % len(wind)]
        # print(w)
        if w == "<":
            x -= 1
        else:
            x += 1
        if not put(f, x, y):
            x = px
            put(f, x, y)
        erase(f, x, y)
        py = y
        y -= 1
        # print("v")
        if not put(f, x, y):
            y = py
            put(f, x, y)
            top = max([p[1] for p in m.keys()]) + 1
            # draw(m)
            Pn = 11
            if i < Pn:
                break
            h = hash(m, top-1, Pn)
            if updHahses(h, n, top-1):
                dn = hashes[h][1][0] - hashes[h][0][0]
                dt = hashes[h][1][1] - hashes[h][0][1]
                print(n, top, hashes[h], dn, dt)
                E = 1000000000000 - n - ((1000000000000 - n) // dn) * dn
                topDelta = dt * ((1000000000000 - n) // dn)

                # for v in hashes[h]:
                #     print(hash(m, v[1], Pn))
                #     draw(m, v[1], Pn)

            break

print(E)

for n in range(n, n+E):
    f = figz[n % len(figz)]
    x = 2
    y = top + 3
    while True:
        i += 1
        erase(f, x, y)
        px = x
        w = wind[i % len(wind)]
        # print(w)
        if w == "<":
            x -= 1
        else:
            x += 1
        if not put(f, x, y):
            x = px
            put(f, x, y)
        erase(f, x, y)
        py = y
        y -= 1
        # print("v")
        if not put(f, x, y):
            y = py
            put(f, x, y)
            top = max([p[1] for p in m.keys()]) + 1
            # draw(m)
            break

print(top + topDelta)
print(1514285714288)
