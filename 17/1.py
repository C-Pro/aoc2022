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


def draw(m):
    h = max(6, max([p[1] for p in m.keys()]))
    w = 7  # max([p[0] for p in m.keys()])
    for y in range(h, -1, -1):
        print("|", end="")
        for x in range(w):
            if m.get((x, y)) == "#":
                print("#", end="")
            else:
                print(".", end="")
        print(f"|{y}", end="")
        print()
    for x in range(w+2):
        print("-", end="")
    print()


def put(m, f, x, y):
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


def erase(m, f, x, y):
    h = len(f)
    w = len(f[0])
    mm = {}
    for yy, r in enumerate(f):
        for xx, c in enumerate(r):
            if c == "#":
                pos = (x+xx, y+yy)
                if pos in m.keys():
                    del (m[pos])


top = 0
i = -1
for n in range(2022):
    f = figz[n % len(figz)]
    x = 2
    y = top + 3
    while True:
        i += 1
        erase(m, f, x, y)
        px = x
        w = wind[i % len(wind)]
        # print(w)
        if w == "<":
            x -= 1
        else:
            x += 1
        if not put(m, f, x, y):
            x = px
            put(m, f, x, y)
        erase(m, f, x, y)
        py = y
        y -= 1
        # print("v")
        if not put(m, f, x, y):
            y = py
            put(m, f, x, y)
            top = max([p[1] for p in m.keys()])+1
            # draw(m)
            break

print(top)
