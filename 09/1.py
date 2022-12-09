import re
from collections import deque

cmds = []


def getints(line):
    return [int(s) for s in re.findall("[0-9]+", line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for line in lines:
        cmds.append((line[0], int(line[2:])))

visited = set([])
head = (1000, 1000)
tail = (1000, 1000)


def moveTail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail

    if dx == 2:
        return (tail[0]+1, head[1])
    if dx == -2:
        return (tail[0]-1, head[1])
    if dy == 2:
        return (head[0], tail[1]+1)
    if dy == -2:
        return (head[0], tail[1]-1)


for cmd in cmds:
    if cmd[0] == "U":
        for step in range(cmd[1]):
            head = (head[0], head[1]+1)
            tail = moveTail(head, tail)
            visited.add(tail)
    if cmd[0] == "D":
        for step in range(cmd[1]):
            head = (head[0], head[1]-1)
            tail = moveTail(head, tail)
            visited.add(tail)
    if cmd[0] == "R":
        for step in range(cmd[1]):
            head = (head[0]+1, head[1])
            tail = moveTail(head, tail)
            visited.add(tail)
    if cmd[0] == "L":
        for step in range(cmd[1]):
            head = (head[0]-1, head[1])
            tail = moveTail(head, tail)
            visited.add(tail)

print(len(visited))
