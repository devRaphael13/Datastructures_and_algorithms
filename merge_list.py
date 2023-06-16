snums1 = [1, 3, 4, 0, 0, 0]
m = 3
nums2 = [2,5,6]
n = 3

def merge(nums1, m, nums2, n):
    del nums1[m:]
    del nums2[n:]
    nums1.extend(nums2)

    if not m or not n:
        return nums1

    nums1.sort()
    return nums1

print(merge(nums1, m, nums2, n))
