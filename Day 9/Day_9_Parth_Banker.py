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
    print("v2")
elif int(v22)<int(v11):
    print("v1")
else:
    print("both")