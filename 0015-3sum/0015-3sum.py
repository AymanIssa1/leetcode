class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        output = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    sub_arr = [nums[i], nums[left], nums[right]]
                    if sub_arr not in output:
                        output.append(sub_arr)
                    right -= 1
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return output
            

        