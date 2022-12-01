a = []
with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    s = 0
    for l in lines:
        c = 0
        try:
            c = int(l)
        except:
            None
        if c == 0:
            a.append(s)
            s = 0
            continue
        s += c

print(sum(sorted(a)[-3:]))
