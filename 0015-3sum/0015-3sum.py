class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = []
        
        nums.sort()

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    arr = [nums[i], nums[left], nums[right]]
                    if arr not in output:
                        output.append(arr)
                
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
                

        return output
        