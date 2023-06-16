nums = [0,0,1,1,1,2,2,2,3,3,3,4,4]

def remove_duplicates(nums):
    i = 0
    j = 1
    k = 0

    while j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(j)
            k += 1
        else:
            i += 1
            j += 1
    nums.extend(list("_" * k))
    return len(nums) - k, nums

print(nums, remove_duplicates(nums))
