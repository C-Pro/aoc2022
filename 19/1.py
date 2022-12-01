with open("input.txt", "rt") as fi:
    lines=fi.read().splitlines()
    a = [int(l) for l in lines]

print(a)
