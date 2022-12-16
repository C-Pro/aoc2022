import itertools
import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


f = {}
m = {}
mem = {}

with open("test.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for line in lines:
        if line == "":
            continue
        fr = getints(line)[0]
        v = line[6:8]
        f[v] = fr
        m[v] = [x.strip() for x in line[line.index("valve")+6:].split(",")]

mem = {}


def dfs(c1, c2, cnt1, cnt2, o):
    if cnt1 + cnt2 < 2:
        return 0

    print(c1, c2, cnt1, cnt2)
    ms = 0
    for (h, e) in itertools.product(*[[True, False], [True, False]]):
        cntI1 = cnt1
        cntI2 = cnt2
        s = 0
        if h:
            if c1 in o:
                continue
            cntI1 -= 1
        if e:
            if c2 in o:
                continue
            cntI2 -= 1

        no = o
        if h and cntI1 > 0:
            no |= set([c1])
            s += f[c1] * cntI1

        if e and cntI1 > 0:
            no |= set([c2])
            s += f[c2] * cntI2

        kn = "".join(sorted(no))
        for hc in m[c1] if cntI1 > 1 else [c1]:
            for ec in m[c2] if cntI2 > 1 else [c2]:
                cntA = cntI1-1 if cntI1 > 1 else 0
                cntB = cntI2-1 if cntI2 > 1 else 0
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
