arr = [ 1, 0, 1, 0, 1, 0, 0, 1 ]


def sortArray(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

sortArray(arr)
print(arr)  