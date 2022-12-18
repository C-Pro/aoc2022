import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("[0-9]+", line)]


s = {
    0: {},
    1: {},
    2: {},
}

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = [getints(l) for l in lines]

area = 0
for i, r in enumerate(a):
    area += 6
    for j, k in enumerate([(0, 1), (0, 2), (1, 2)]):
        key = str(r[k[0]]).rjust(2, "0") + str(r[k[1]]).rjust(2, "0")
        v = s[j].get(key)
        if v is None:
            s[j][key] = set([i])
            continue
        s[j][key].add(i)

x = set([])
o = [2, 1, 0]
for r in a:
    for j, k in enumerate([(0, 1), (0, 2), (1, 2)]):
        key = str(r[k[0]]).rjust(2, "0") + str(r[k[1]]).rjust(2, "0")
        v = s[j].get(key)
        if v is not None:
            for p in v:
                if r[o[j]] - a[p][o[j]] == 1:
                    x.add(str(r)+str(a[p]))
                    x.add(str(a[p])+str(r))

print(area - len(x))
