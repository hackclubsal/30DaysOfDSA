'''Input : [0,1,1,0,0,1,0]'''
'''Output : [0,0,0,0,1,1,1]'''
def sortarr(a,n):
    j = -1
    for i in range(len(arr)):
        if a[i] < 1:
            j = j + 1
            a[i], a[j] = a[j], a[i]

arr = [0,1,1,0,0,1,0]
n = len(arr)
sortarr(arr,n)
for i in range(n):
        print(arr[i], end = " ")