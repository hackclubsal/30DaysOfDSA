# changed k=4 to get the desired output.
def rotate(arr, limit, size):
    for i in range(0,limit+1):
        temp = arr[0]
        for j in range(size-1):
            arr[j] = arr[j+1]
        arr[size-1] = temp
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
k = 4
N = len(arr)
# Function call
arr = rotate(arr, k, N)
for i in arr:
    print(i, end=" ")

