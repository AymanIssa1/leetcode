class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
