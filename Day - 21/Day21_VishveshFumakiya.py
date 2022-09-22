def fib(s):
    if s <= 1:
        return s
    return fib(s-1) + fib(s-2)
def countWays(n):
    return fib(n + 1)
n = 4
print("Answer :", countWays(n))
