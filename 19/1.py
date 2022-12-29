import re
from collections import deque

b = []

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for l in lines:
        bp = {}
        parts = l.split(":")[1].split(".")
        for part in parts:
            part = part.strip()
            if len(part) < 1:
                continue
            name = part.split(" ")[1]
            matches = re.findall(r"[\d]+ [\w]+", part)
            req = {}
            for m in matches:
                n, r = m.split(" ")
                req[r] = int(n)
            bp[name] = req
        b.append(bp)


def canBuild(bp, ore):
    l = []
    for o, req in bp.items():
        for r, n in req.items():
            enough = True
            if ore.get(r, 0) < n:
                enough = False
                break
        if enough:
            l.append(o)
    return l


def addRobot(robots, robot):
    nr = {r: n for r, n in robots.items()}
    amt = nr.get(robot, 0)
    nr[robot] = amt + 1
    return nr


def spendOre(ore, p):
    no = {o: n for o, n in ore.items()}
    for o, n in p.items():
        no[o] -= n
        assert (no[o] >= 0)
    return no


def k(s, r, o):
    ol = []
    for n in ["ore", "clay", "obsidian", "geode"]:
        ol.append(str(o.get(n, 0)))
    os = ",".join(ol)

    rl = []
    for n in ["ore", "clay", "obsidian", "geode"]:
        rl.append(str(r.get(n, 0)))
    rs = ",".join(rl)

    return f"{s}:{rs}:{os}"


def dfs(bp, steps, robots, ore):
    if steps == 0:
        return ore.get("geode", 0)

    ks = k(steps, robots, ore)
    c = cache.get(ks)
    if c is not None:
        return c

    cb = canBuild(bp, ore)
    for r, n in robots.items():
        amt = ore.get(r, 0)
        ore[r] = amt + n

    best = 0
    for r in cb:
        g = dfs(bp, steps-1, addRobot(robots, r), spendOre(ore, bp[r]))
        if g > best:
            best = g

    g = dfs(bp, steps-1, robots, ore)
    if g > best:
        best = g

    cache[ks] = best

    return best


cache = None
i = 0
q = 0
for bp in b:
    cache = {}
    i += 1
    b = dfs(bp, 24, {"ore": 1}, {})
    print(i, b)
    q += b * i
print(q)
