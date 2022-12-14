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
    srt = sorted(l)
    if lis((srt[0], srt[-1])) in (lis(l[:2]), lis(l[2:])):
        s += 1
print(s)
