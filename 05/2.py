import re
from collections import deque

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

state = 0
stacks = {}
for line in lines:
    if state == 0:
        if len(re.findall("[0-9]+", line)) > 0:
            labels = list(re.findall("[0-9]+", line))
            state += 1
            continue

        l = list(line)
        for i in range(len(line)):
            if i % 4 == 0:
                l[i] = "["
            if (i+2) % 4 == 0:
                l[i] = "]"

        line = "".join(l)
        matches = re.findall("\[[^\[\]]+\]", line)
        if len(matches) > 0:
            for i, m in enumerate(matches):
                if i not in stacks.keys():
                    stacks[i] = deque()
                if m[1] not in (' ', '\t'):
                    stacks[i].appendleft(m[1])
    else:
        rule = list(re.findall("[0-9]+", line))
        if len(rule) != 3:
            continue
        cnt = int(rule[0])
        f = int(rule[1])-1
        t = int(rule[2])-1
        d = deque([])
        for _ in range(cnt):
            d.append(stacks[f].pop())
        for _ in range(cnt):
            stacks[t].append(d.pop())


print("".join([stacks[i].pop() for i in range(len(stacks))]))
