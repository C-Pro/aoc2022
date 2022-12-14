import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


msgs = []

with open("input.txt", "rt") as fi:
    groups = fi.read().split("\n\n")
    for group in groups:
        g = []
        for line in group.splitlines():
            g.append(eval(line))
        msgs.append(g)


def right(m1, m2):
    if type(m1) == type(m2) == int:
        if m1 == m2:
            return None
        return m1 < m2
    if type(m1) == int and type(m2) == list:
        return right([m1], m2)
    if type(m1) == list and type(m2) == int:
        return right(m1, [m2])
    if type(m1) == type(m2) == list:
        for i in range(min(len(m1), len(m2))):
            r = right(m1[i], m2[i])
            if r is None:
                continue
            return r
        if len(m2) < len(m1):
            return False
        return True

s = 0
for i, msg in enumerate(msgs):
    #print(i, right(msg[0], msg[1]))
    if right(msg[0], msg[1]):
        s += i+1


print(s)
