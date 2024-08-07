class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        output = []
        
        for i in range(n-3):
            # Avoid duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n-2):
                # Avoid duplicates for the second number
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                # Two-pointer approach
                left, right = j + 1, n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Avoid duplicates for the third and fourth numbers
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return output
