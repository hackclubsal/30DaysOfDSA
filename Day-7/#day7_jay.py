num = int(input("Enter a number: "))
box = 0

while num > 0:
	rem = num % 10
	box = box * 10 + rem
	num = int(num/10)

print("Reverse of entered number:", box)
