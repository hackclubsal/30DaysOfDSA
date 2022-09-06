s = "/you/are\\how\\"
s = s[1:-1]
s = s.replace("/", " ")
s = s.replace("\\", " ")
li = list(s.split(" "))
li.reverse()
res = ' '.join(map(str, li))
res = res.replace(" ","")
print(res)
