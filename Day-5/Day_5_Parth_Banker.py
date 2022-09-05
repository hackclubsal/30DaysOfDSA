arr = [1,1,2,3,3,4,4,5,5]

index = 0

for i in arr:
    a = 0
    for j in arr:
        if i == j:
            a+=1
    if a==1:
        index=i
        break

print("The index of the number that occurs only once is",index)


