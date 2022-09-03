'''Rotate array to right with k steps'''
def RotateArr(Arr, k):
 
    if k < 0 or k >= len(Arr):
        return
 
    for i in range(k):
        last = Arr[-1]
        for i in reversed(range(len(Arr) - 1)):
            Arr[i + 1] = Arr[i]
 
        Arr[0] = last
 
if __name__ == '__main__':
 
    Arr = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 4
 
    RotateArr(Arr, k)
    print(Arr)
