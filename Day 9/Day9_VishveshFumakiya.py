#Given two version numbers, compare them.
def verComp(v1, v2):
	a1 = v1.split(".")
	a2 = v2.split(".")
	n = len(a1)
	m = len(a2)

	a1 = [int(i) for i in a1]
	a2 = [int(i) for i in a2]
	
	for i in range(len(a1)):
		if(a1[i]>a2[i]):
			return 1
		elif(a1[i]<a2[i]):
			return -1
	return 0

ver1 = "1.1.0"
ver2 = "1.2.0"

res = verComp(ver1, ver2)
if(res < 0):
	print("Version 2 > Version 1")
elif(res > 0):
	print("Version 2 < Version 1")
else:
	print("Both are equal")
