import math

def isPerfectSquare(x):

	if(x >= 0):
		sr = int(math.sqrt(x))
			return ((sr*sr) == x)
	
    return false

x = 55;
if (isPerfectSquare(x)):
	print("True")
else:
	print("False")
