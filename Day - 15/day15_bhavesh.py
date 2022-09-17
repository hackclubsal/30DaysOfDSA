def printIntersection(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j+= 1
        else:
            print(arr2[j],end=" ")
            j += 1
            i += 1
 
# Driver program to test above function
arr1 = [1, 3, 4, 5, 5, 6, 6, 7]
arr2 = [2, 5, 6, 6, 7, 8]
m = len(arr1)
n = len(arr2)
printIntersection(arr1, arr2, m, n)
