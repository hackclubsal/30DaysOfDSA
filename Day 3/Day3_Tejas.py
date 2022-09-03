def checkKey(a,n):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == n:
                return True
            





A = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]

n = int(input("Key: "))

if checkKey(A,n):
    print("key Found")
else:
    print("not found")


