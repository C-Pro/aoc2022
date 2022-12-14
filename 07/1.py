import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("[0-9]+", line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

sizes = {}
currpath = deque([])
state = None
for line in lines:
    cd = re.match("\$ cd (.+)", line)
    ls = re.match("\$ ls", line)

    if cd:
        state = "cd"
        if cd[1] == "..":
            currpath.pop()
        else:
            currpath.append(cd[1])
        continue

    if ls:
        state = "ls"
        continue

    i = getints(line)
    if i:
        key = "/".join(currpath)
        if key.startswith("//"):
            key = key[1:]
        if key not in sizes.keys():
            sizes[key] = i[0]
        else:
            sizes[key] += i[0]

if "/" not in sizes.keys():
    sizes["/"] = 0
for (k, v) in list(sizes.items()):
    if k == "/":
        continue
    k = ["/" if s == "" else s for s in k.split("/")]
    while len(k) > 1:
        k.pop()
        key = "/".join(k)
        if key.startswith("//"):
            key = key[1:]
        if key not in sizes.keys():
            sizes[key] = v
        else:
            sizes[key] += v

print(sum([v for (k, v) in sizes.items() if v <= 100000]))
