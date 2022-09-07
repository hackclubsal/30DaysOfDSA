def search(list, n):
    temp = -1
    for i in range(0, n, 2):
        if (list[i] != list[i + 1]):
            temp = list[i]
            break
    if(list[n-2] != list[n-1]):
        temp = list[n-1]
 
    print(temp)

list = [1, 1, 2, 3, 3, 4, 4]
Len = len(list)
 
search(list, Len)
