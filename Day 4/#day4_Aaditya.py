def isPerfectSquare(n):
    if n < 0:
        return False
    for i in range(1, int(n /3)):
        if i * i == n:
            return True

    return False

n = int(input("Enter num:"))
print(isPerfectSquare(n))
