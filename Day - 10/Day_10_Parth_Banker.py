s = "bcabc"

t = set({})

for char in s:
    t.add(char)

t = list(sorted(t))

s = ''.join([str(elem) for elem in t])

print(s)