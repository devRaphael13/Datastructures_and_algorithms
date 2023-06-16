nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

def remove_duplicatesII(nums):
    i = 0
    j = 1
    k = 2
    spaces = 0

    while k < len(nums):
        if nums[i] == nums[j] == nums[k]:
            nums.pop(k)
            spaces += 1
        else:
            i += 1
            j += 1
            k += 1
    nums.extend(["_" for i in range(spaces)])
    return len(nums) - spaces, nums

print(remove_duplicatesII(nums))

