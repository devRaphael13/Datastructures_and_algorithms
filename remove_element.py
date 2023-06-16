nums = [0,1,2,2,3,0,4,2]
val = 2
# Output: 5 nums = [0,1,4,0,3,_,_,_]


nums = [0,1,2,2,3,0,4,2]
val = 2

def remove_element(nums, val):
    i = 0
    j = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            nums.append("_")
            j += 1
        else:
            i += 1
    return len(nums) - j

print(remove_element(nums, val))


