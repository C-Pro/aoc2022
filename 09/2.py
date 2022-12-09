import re
from collections import deque

cmds = []

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    for line in lines:
        cmds.append((line[0], int(line[2:])))

visited = set([])
parts = [(1000, 1000)]*10

def moveTail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail

    if abs(dx) + abs(dy) < 4:
        if dx == 2:
            return (tail[0]+1, head[1])
        if dx == -2:
            return (tail[0]-1, head[1])
        if dy == 2:
            return (head[0], tail[1]+1)
        if dy == -2:
            return (head[0], tail[1]-1)

    return (tail[0]+dx//2, tail[1]+dy//2)




for x, cmd in enumerate(cmds):
    #print(x, cmd, parts)
    if cmd[0] == "U":
        for step in range(cmd[1]):
            for i in range(9):
                head = parts[i]
                tail = parts[i+1]
                if i == 0:
                    head = (head[0], head[1]+1)
                tail = moveTail(head, tail)
                parts[i] = head
                parts[i+1] = tail
            visited.add(tail)
    if cmd[0] == "D":
        for step in range(cmd[1]):
            for i in range(9):
                head = parts[i]
                tail = parts[i+1]
                if i == 0:
                    head = (head[0], head[1]-1)
                tail = moveTail(head, tail)
                parts[i] = head
                parts[i+1] = tail
            visited.add(tail)
    if cmd[0] == "R":
        for step in range(cmd[1]):
            for i in range(9):
                head = parts[i]
                tail = parts[i+1]
                if i == 0:
                    head = (head[0]+1, head[1])
                tail = moveTail(head, tail)
                parts[i] = head
                parts[i+1] = tail
            visited.add(tail)
    if cmd[0] == "L":
        for step in range(cmd[1]):
            for i in range(9):
                head = parts[i]
                tail = parts[i+1]
                if i == 0:
                    head = (head[0]-1, head[1])
                tail = moveTail(head, tail)
                parts[i] = head
                parts[i+1] = tail
            visited.add(tail)

print(len(visited))
