with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = [(l[0], l[2]) for l in lines]

# x- lose, y - draw, z - win
M = {
    "AX": 0 + 3, # rs
    "AY": 3 + 1, # rr
    "AZ": 6 + 2, # rp
    "BX": 0 + 1, # pr
    "BY": 3 + 2, # pp
    "BZ": 6 + 3, # ps
    "CX": 0 + 2, # sp
    "CY": 3 + 3, # ss
    "CZ": 6 + 1, # sr
}

score = 0
for v in a:
    score += M[f"{v[0]}{v[1]}"]

print(score)
