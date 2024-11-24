class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        nums.sort()

        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) -1
            while left < right:
                sum = nums[left] + nums[right] + nums[index]
                if sum < target:
                    result += (right - left)
                    left += 1 
                else:
                    right -= 1

        return result 
        