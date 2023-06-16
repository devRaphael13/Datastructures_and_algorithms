nums = [2,2,1,1,1,2,2]
#Output: 2

nums = [3,2,3]
nums = [3, 3, 4]
nums = [6, 5, 5]

def majority_element(nums):
    majority = 0
    x = 0

    for i in nums:
        y = nums.count(i)
        if y > x:
            majority = i
            x = y
    return majority

def majority(nums):
    unique = list(set(nums))
    max = 0
    celeb = 0

    for num in unique:
        count = nums.count(num)
        if max < count > len(nums) // 2:
            return num

        if count > max:
            celeb = num
            max = count
    return celeb
print(majority(nums))

