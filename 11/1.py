import re
import math
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


monkeys = []


def op(val, s):
    old = val
    return eval(s)


with open("input.txt", "rt") as fi:
    parts = fi.read().split("\n\n")
    for part in parts:
        lines = part.splitlines()
        items = getints(lines[1])
        monkey = {
            "items": deque(items),
            "operation": lines[2].split("=")[1].strip(),
            "div": getints(lines[3])[0],
            "true": getints(lines[4])[0],
            "false": getints(lines[5])[0],
            "cnt": 0,
        }
        monkeys.append(monkey)

for i in range(20):
    for monkey in monkeys:
        while len(monkey["items"]) > 0:
            monkey["cnt"] += 1
            item = monkey["items"].popleft()
            item = op(item, monkey["operation"])
            item = item//3

            if item % monkey["div"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)

monkeys.sort(key=lambda x: -x["cnt"])
print(monkeys[0]["cnt"] * monkeys[1]["cnt"])
