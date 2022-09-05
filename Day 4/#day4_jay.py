def perfectSquare(x):
	a = 1
	b = x
	while (a <= b):
		c = (a + b) >> 1

		# if c is Perfect square
		if ((c ** 2) == x):
			return True

		# c is small --> go b to increase c
		if (c ** 2 < x):
			a = c + 1

		# c is large --> to a to decrease c	
		else:
			b = c - 1

	return False

num = int(input("Enter number: "))

if (perfectSquare(num)):
	print(num, "is a perfect square")

else:
	print(num, "is not a perfect square")




