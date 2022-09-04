# Given a positive integer num, write a function that returns true if num is a perfect square else false.

class isPerfectSquare:
    def __init__(self, n):
        self.n = n

    def isPerfectSquare(self):
        for i in range(self.n//2):
            if i*i == self.n:
                return True
        return False


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    obj = isPerfectSquare(n)
    print(obj.isPerfectSquare())
