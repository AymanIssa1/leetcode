class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = []
        
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate elements
                
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    arr = [nums[i], nums[left], nums[right]]
                    if arr not in output:
                        output.append(arr)
                
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    arr = [nums[i], nums[left], nums[right]]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # skip duplicate elements
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # skip duplicate elements
                    left += 1
                    right -= 1
                

        return output
        