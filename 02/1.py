with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()
    a = [(l[0], l[2]) for l in lines]

M = {
    "AX": 3, # rr
    "AY": 6, # rp
    "AZ": 0, # rs
    "BX": 0, # pr
    "BY": 3, # pp
    "BZ": 6, # ps
    "CX": 6, # sr
    "CY": 0, # sp
    "CZ": 3, # ss
}

S = {"X": 1, "Y": 2, "Z": 3}

score = 0
for v in a:
    score += S[v[1]] + M[f"{v[0]}{v[1]}"]

print(score)
