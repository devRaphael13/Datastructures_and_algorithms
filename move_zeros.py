nums = [0,1,0,3,12]
#nums = [0, 0, 1]

def move_zeros(nums):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            j -= 1
        else:
            i += 1
    return nums

print(move_zeros(nums))

