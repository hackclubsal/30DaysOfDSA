mylist = [1,0,1,0,1,0,0,1]
print(mylist)
for i in range(0, 8):
	mylist[i]
 
	for j in range(i+1,8):
		if mylist[j] < mylist[i]:
			c = mylist[i]
			mylist[i] = mylist[j]
			mylist[j] = c
 
print(mylist)
