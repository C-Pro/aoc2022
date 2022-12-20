import itertools
import re
from collections import deque
from math import inf


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


f = {}
m = {}
mem = {}

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for line in lines:
        if line == "":
            continue
        fr = getints(line)[0]
        v = line[6:8]
        f[v] = fr
        m[v] = [x.strip() for x in line[line.index("valve")+6:].split(",")]

mem = {}
dists = {}


def dj(s, e):
    unvisited = set(m.keys())
    dists = {p: inf for p in unvisited}
    dists[s] = 0
    curr = s
    while len(unvisited) > 0:
        for p in m[curr]:
            if dists[p] > dists[curr] + 1:
                dists[p] = dists[curr] + 1
        unvisited.remove(curr)
        if len(unvisited) == 0:
            return dists
        if min([dists[p] for p in unvisited]) == inf:
            print("unreachable nodes detected")
            return dists
        curr = sorted([(p, d) for p, d in dists.items()
                      if p in unvisited], key=lambda x: x[1])[0][0]
    return dists


def gkey(s, e):
    "distance key for non directional graph"
    return tuple(sorted([s, e]))


for s in f.keys():
    for e in f.keys():
        if e == s:
            continue
        dists.update({gkey(s, e): v for k, v in dj(s, e).items()})


def dfs(c1, c2, cnt1, cnt2, o):
    if cnt1 < 2 and cnt1 < 2:
        return 0

    #print(c1, c2, cnt1, cnt2)
    closed = set(f.keys()) - set(o)

    try:
        if cnt1 < min([dists[gkey(c1, c)] for c in closed if c != c1]) + 2 and \
                cnt2 < min([dists[gkey(c2, c)] for c in closed if c != c2]) + 2:
            return 0
    except:
        None

    if len(o) == len(f):
        return 0

    ms = 0
    for (h, e) in itertools.product(*[[True, False], [True, False]]):
        cntI1 = cnt1
        cntI2 = cnt2
        s = 0
        no = set(o)
        if h and cntI1 > 0 and c1 not in no:
            cntI1 -= 1
            no |= set([c1])
            s += f[c1] * cntI1

        if e and cntI2 > 0 and c2 not in no:
            cntI2 -= 1
            no |= set([c2])
            s += f[c2] * cntI2

        kn = "".join(sorted(no))
        for hc in m[c1] if cntI1 > 1 else [c1]:
            for ec in m[c2] if cntI2 > 1 else [c2]:
                cntA = (cntI1-1) if cntI1 > 1 else 0
                cntB = (cntI2-1) if cntI2 > 1 else 0
                if cntA == cntB == 0:
                    continue
                key = hc + ec + "." + str(cntA) + \
                    "."+str(cntB) + kn
                sx = mem.get(key)
                if sx is None:
                    sx = dfs(hc, ec, cntA, cntB, no)
                    mem[key] = sx
                sn = sx + s
                if sn > ms:
                    ms = sn

    return ms


print(dfs("AA", "AA", 26, 26, set([])))
