class Solution:
def findLengthOfLCIS(nums):
    if not nums: 
        return 0
    
    max_length = 0
    current_length = 1 
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    return max(max_length, current_length)