def RightShift(ar,n):
    for i in range(n):
        LE = ar[len(ar)-1]

        for j in range(len(ar)-1 , -1 , -1):
            ar[j] = ar[j-1]
        
        ar[0] = LE
    
    return ar


A = [1,2,3,4,5,6,7]

n = int(input("How much you want to skip?"))
print("-----RightShiftedArray----")
print(RightShift(A,n))