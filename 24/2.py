from collections import deque

m = {}


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for r, line in enumerate(lines):
        m.update({(r, c): [v] for c, v in enumerate(
            line) if v in ("<", ">", "^", "v")})

H = len(lines)
W = len(lines[0])

START = (0, 1)
END = (H-1, W-2)


def warpR(r):
    return (r - 1) % (H - 2) + 1


def warpC(c):
    return (c - 1) % (W - 2) + 1


moves = {
    "^": lambda x, n: (warpR(x[0]-n), x[1]),
    "v": lambda x, n: (warpR(x[0]+n), x[1]),
    "<": lambda x, n: (x[0], warpC(x[1]-n)),
    ">": lambda x, n: (x[0], warpC(x[1]+n)),
}


def getMap(m, steps):
    nm = {}
    for c, v in m.items():
        for b in v:
            mv = moves[b]
            nc = mv(c, steps)
            if nc not in nm.keys():
                nm[nc] = []
            nm[nc].append(b)
    return nm


def draw(m, E=START):
    def pr(s):
        print(s, end="")
    for r in range(H):
        for c in range(W):
            p = (r, c)
            if p == E:
                pr("E")
                continue
            if p == START:
                pr(".")
                continue
            if p == END:
                pr(".")
                continue
            if r in (0, H-1):
                pr("#")
                continue
            if c in (0, W-1):
                pr("#")
                continue
            v = m.get(p)
            if v is None:
                pr(".")
                continue
            if len(v) == 1:
                pr(v[0])
                continue
            pr(len(v))
        print()


maps = [m]


def getWays(c, m):
    ways = []
    for o in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nc = (c[0]+o[0], c[1]+o[1])
        if nc[0] <= 0 or nc[0] >= H-1:
            continue
        if nc[1] <= 0 or nc[1] >= W-1:
            continue
        if nc not in m.keys():
            ways.append(nc)
    if c not in m.keys():
        ways.append(c)
    return ways


def dfs(S, E, step, maps):
    v = set()
    c = S
    q = deque([(c, step)])
    while len(q) > 0:
        c, step = q.pop()
        if (c, step) in v:
            continue
        v.add((c, step))
        # print(step, c)
        # draw(maps[step], c)
        if c == E:
            return (step+1)
            exit()

        if len(maps) < step + 2:
            maps.append(getMap(m, step+1))
        ways = getWays(c, maps[step+1])
        for w in ways:
            q.appendleft((w, step+1))


s1 = dfs(START, (H-2, W-2), 0, maps)
s2 = dfs(END, (1, 1), s1, maps)
s3 = dfs(START, (H-2, W-2), s2, maps)
print(s3)
