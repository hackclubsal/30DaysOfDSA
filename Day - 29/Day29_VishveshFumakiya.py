def findMin(s, l, h):
    if(l == h):
       return 0

    if (l == h - 1):
       return 0 if(s[l] == s[h]) else 1

    if(s[l] == s[h]):
       return findMin(s, l + 1, h - 1)
    else:
       return (min(findMin(s,l, h - 1), findMin(s, l + 1, h)) + 1)

s = "baaba"
print(findMin(s, 0, len(s) - 1))
