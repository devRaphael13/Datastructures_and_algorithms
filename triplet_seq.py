nums = [1, 2, 3, 4, 5] #True
#nums = [5, 4, 3, 2,1] #False
#nums = [2, 1, 5, 0, 4, 6] #True
#nums = [20, 100, 10, 12, 5, 13] #True

def increasing_triplet(nums):
	first = float("inf")
	second = float("inf")

	for num in nums:
		if num <= first:
			first = num
		elif num <= second:
			second = num
		else:
			return True
	return False

print(increasing_triplet(nums))

