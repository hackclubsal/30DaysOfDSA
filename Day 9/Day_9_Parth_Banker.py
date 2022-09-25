v1 = "1.0008.0"
v2 = "1.004.0"

v1 = v1.split('.')
v2 = v2.split('.')

v11 = ""
v22 = ""

for (a,b) in zip(v1, v2):
    v11 += str(int(a))
    v22 += str(int(b))

if int(v22)>int(v11):
    print("Version 2 > Version 1")
elif int(v22)<int(v11):
    print("Version 2 < Version 1")
else:
    print("Version 2 = Version 1")