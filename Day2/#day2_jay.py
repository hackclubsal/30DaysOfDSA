num = [1,2,3,4,5,6,7]

shift = 3

def rightArrayRotation(num_array, shift):
	for i in range(0, shift):
		temp = num_array[len(num_array)-1]
		for j in range(len(num_array)-1, 0, -1):
			num_array[j] = num_array[j-1]

		num_array[0] = temp

	return num_array

def printArray(array):
	for i in range(0,len(array)):
		print(array[i], end=' ')

print("Array Before rotation: ")
printArray(num)

rotated_array = rightArrayRotation(num, shift)
print("\nArray After rotation: ")
printArray(rotated_array)
