class Solution:
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    result = set1 & set2

    return list(result)