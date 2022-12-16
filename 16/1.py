import re
from collections import deque


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


def dfs(c, cnt, o):
    if cnt < 2:
        return 0
    if cnt == 2:
        if c not in o:
            return f[c]
        return 0

    # max flow if we open current valve

    maxF = 0
    if f[c] > 0 and c not in o:
        no = o | set([c])
        for n in m[c]:
            key = n + str(cnt-2) + "".join(sorted(no))
            s = mem.get(key)
            if s is None:
                s = dfs(n, cnt-2, no)
                mem[key] = s
            if s > maxF:
                maxF = s
        maxF = maxF + f[c] * (cnt-1)

    # max flow if we don't open current valve
    maxF2 = 0
    for n in m[c]:
        key = n + str(cnt-1) + "".join(sorted(o))
        s = mem.get(key)
        if s is None:
            s = dfs(n, cnt-1, o)
            mem[key] = s
        if s > maxF2:
            maxF2 = s

    return max(maxF, maxF2)


print(dfs("AA", 30, set([])))
