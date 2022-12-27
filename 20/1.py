import copy
import re
from collections import deque


def getints(line):
    return [int(s) for s in re.findall("-?[0-9]+", line)]


with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = [getints(l)[0] for l in lines]


class E(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val)


head = None
prev = None
for v in a:
    n = E(v, prev, None)
    if prev is not None:
        prev.next = n
    if head is None:
        head = n
    prev = n

tail = n
tail.next = head
head.prev = tail


def pr(head):
    b = []
    c = None
    while c != head:
        if c is None:
            c = head
        print(c.val, end=" ")
        b.append(c)
        c = c.next
    print()
    return b


b = pr(head)

print(sum([x.val for x in b]))

for v in b:
    if v.val == 0:
        continue
    if v == head:
        head = v.next
    elif v == tail:
        tail = v.prev
    if v.val > 0:
        c = v
        for i in range(v.val):
            c = c.next

        vc = copy.copy(v)
        cc = copy.copy(c)

        v.next.prev = vc.prev
        v.prev.next = vc.next
        v.prev = c
        v.next = cc.next
        c.next.prev = v
        c.next = v
    if v.val < 0:
        c = v
        for i in range(abs(v.val)):
            c = c.prev
        vc = copy.copy(v)
        cc = copy.copy(c)

        v.prev.next = vc.next
        v.next.prev = vc.prev
        v.next = c
        v.prev = cc.prev
        c.prev.next = v
        c.prev = v


b = [x.val for x in pr(head)]

print(sum(b))

n = len(b)
z = b.index(0)
print(b[(z+1000) % n])
print(b[(z+2000) % n])
print(b[(z+3000) % n])
print(b[(z+1000) % n]+b[(z+2000) % n]+b[(z+3000) % n])
