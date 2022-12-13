import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


msgs = []

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for line in lines:
        if line.strip() == "":
            continue
        msgs.append(eval(line))


msgs.append([[2]])
msgs.append([[6]])


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
        if len(m1) < len(m2):
            return True
        if len(m1) > len(m2):
            return False
        return None


s = 0
for i in range(len(msgs)-1):
    for j in range(i+1, len(msgs)):
        if right(msgs[i], msgs[j]) == False:
            msgs[i], msgs[j] = msgs[j], msgs[i]

print((msgs.index([[2]])+1) * (msgs.index([[6]])+1))
