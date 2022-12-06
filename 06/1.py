with open("input.txt", "rt") as fi:
    s = fi.read()

for i in range(len(s)-3):
    if len(set(list(s[i:i+4]))) == 4:
        print(s[i:i+4])
        print(i+4)
        break
