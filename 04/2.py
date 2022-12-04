import re
with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = []
    for line in lines:
        nums = re.findall("[0-9]+", line)
        a.append([int(s) for s in nums])


def lis(a):
    return "".join([str(x) for x in a])


s = 0
for l in a:
    l[:2] = sorted(l[:2])
    l[2:] = sorted(l[2:])
    if l[0] > l[2]:
        l = [l[2], l[3], l[0], l[1]]

    if l[0] <= l[3] and l[1] >= l[2]:
        s += 1

print(s)
