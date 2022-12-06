with open("input.txt", "rt") as fi:
    s = fi.read()

for i in range(len(s)-13):
    if len(set(list(s[i:i+14]))) == 14:
        print(s[i:i+14])
        print(i+14)
        break
