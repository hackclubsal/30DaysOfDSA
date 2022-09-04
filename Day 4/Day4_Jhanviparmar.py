'''check if given number is perfect square, without usinh inbuilt function.'''
def isPerfectSquare(n) :
    if n == 0:
        return True
    i = 1
    while(i * i<= n):
        if ((n % i == 0) and (n / i == i)):
            return True
        i = i + 1
    return False

if __name__ == "__main__" :
 
    n =1001
    if (isPerfectSquare(n)):
        print(isPerfectSquare(n))
    elif n == 0:
        print(isPerfectSquare(n))
    else :
        print(isPerfectSquare(n))
