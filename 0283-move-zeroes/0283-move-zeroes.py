class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start, end = 0, 0
        while start < len(nums) and end < len(nums):
            while start < len(nums) and nums[start] != 0:
                start += 1
                end = start + 1

            if end < len(nums) and nums[end] != 0:
                nums[end], nums[start] = nums[start], nums[end]
                start += 1
            end += 1