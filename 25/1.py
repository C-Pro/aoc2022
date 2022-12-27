import re
from collections import deque

digits = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

def fs(line):
    return sum([digits[c]*(5**i) for i,c in enumerate(reversed(line))])

def ts(num):
    s = []
    while num > 0:
        s.append(num % 5)

assert (fs("1=-0-2") == 1747)
assert (fs("12111") == 906)
assert (fs("21") == 11)


with open("test.txt", "rt") as fi:
    lines = fi.read().splitlines()

s = sum([fs(line) for line in lines])
print(s)
