nums = [1,2,3,4,5,6,7]
k = 3
#Output: [5,6,7,1,2,3,4]

def rotate(nums, k):
    while k > 0:
        nums.insert(0, nums.pop(-1))
        k -= 1
    return nums

print(rotate(nums, k))

