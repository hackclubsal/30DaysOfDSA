def search(nums):
	start = 0
	end = len(nums)-1

	while (start <= end):
		mid = start + (end - start) // 2
		
		if (nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
		
			return nums[mid]

		elif((nums[mid] == nums[mid + 1] and mid % 2 == 0) or (nums[mid] == nums[mid - 1] and mid % 2 != 0)):
			start = mid + 1
			
		else:
			end = mid - 1
	
	return -1

arr = [1, 1, 2, 3, 3, 4, 4]
element = search(arr)

if (element != -1):
	print(element)
else:
	print("There is no such element")
