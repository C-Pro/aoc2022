with open("input.txt", "rt") as fi:
    lines = fi.read().splitlines()

s = 0
i = 0
for l in lines:
    if i == 0:
        gr = set([])
        for c in l:
            gr.add(c)
        i += 1
        continue

    gr = gr.intersection(set(l))

    i += 1
    if i == 3:
        i = 0
        assert (len(gr) == 1)
        wrong = gr.pop()
        if wrong.islower():
            priority = ord(wrong)-ord('a')+1
        else:
            priority = ord(wrong)-ord('A')+27
        print(wrong, priority)
        s += priority

print(s)
