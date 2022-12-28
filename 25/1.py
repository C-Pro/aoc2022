digits = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
stigid = {v: k for k, v in digits.items()}


def fs(line):
    return sum([digits[c]*(5**i) for i, c in enumerate(reversed(line))])


assert (fs("1=-0-2") == 1747)
assert (fs("12111") == 906)
assert (fs("21") == 11)


def ts(num):
    s = ""
    um = 0
    while num != 0:
        dig = num % 5
        if dig > 2:
            um = 1
            dig = dig - 5
        s += stigid[dig]
        num = num // 5 + um
        um = 0

    return "".join(reversed(s))


assert (ts(1747) == "1=-0-2")
assert (ts(906) == "12111")
assert (ts(11) == "21")

with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

s = sum([fs(line) for line in lines])
print(ts(s))
