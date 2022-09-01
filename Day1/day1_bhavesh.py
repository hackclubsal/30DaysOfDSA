def sort(A):
 
       zeros = A.count(0)
 
   
    k = 0
    while zeros:
        A[k] = 0
        zeros = zeros - 1
        k = k + 1
 
   
    for k in range(k, len(A)):
        A[k] = 1
 
 
if __name__ == '__main__':
 
    A = [1, 0, 1, 0, 1, 0, 0, 1]
 
    sort(A)
 
    
    print(A)
