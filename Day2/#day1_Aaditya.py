def arrRotate(a, n, t):
    t = t % n;
 
    for i in range(0, n):
 
        if(i < t):
            print(a[n + i - t], end = " ");
 
        else:
            print(a[i - t], end = " ");

Array = [ 1, 2, 3, 4, 5, 6, 7 ];
N = len(Array);
T = 4;  #target value
     
arrRotate(Array, N, T);
 
