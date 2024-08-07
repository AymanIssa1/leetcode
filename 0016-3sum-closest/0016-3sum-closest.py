class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total > target:
                    right -= 1
                else:
                    left += 1

        return closest_sum
        