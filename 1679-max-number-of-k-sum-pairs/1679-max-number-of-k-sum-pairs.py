class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort()
        output = 0
        start, end = 0, len(nums) - 1

        while nums and start < end:
            if nums[start] + nums[end] == k:
                del nums[end]
                del nums[start]
                output += 1
                end -= 2
            elif nums[end] > k:
                end -= 1
            else:
                start += 1
        
        return output