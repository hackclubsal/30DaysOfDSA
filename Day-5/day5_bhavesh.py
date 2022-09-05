'''Find not repeated number in sorted array'''
def searchNum(arr, n):
    ans = -1
    for i in range(0, n, 2):
        if (arr[i] != arr[i + 1]):
            ans = arr[i]
            break
    if(arr[n-2] != arr[n-1]):
        ans = arr[n-1]
 
    # ans = -1 if no such element is present.
    print(ans)

arr = [1, 1, 2, 3, 3, 4, 4]
Len = len(arr)
 
searchNum(arr, Len)
