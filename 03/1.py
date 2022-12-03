with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

s = 0
for l in lines:
    mid = len(l) // 2
    first = l[:mid]
    second = l[mid:]
    assert (len(first) == len(second))
    wrong = set(first).intersection(set(second))
    assert (len(wrong) == 1)
    wrong = list(wrong)[0]
    if wrong.islower():
        priority = ord(wrong)-ord('a')+1
    else:
        priority = ord(wrong)-ord('A')+27
    print(wrong, priority)
    s += priority

print(s)
