class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]

            if curr == target:
                return mid

            # Determine which side is sorted
            if nums[left] <= curr:  # Left side is sorted
                if nums[left] <= target < curr:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right side is sorted
                if curr < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1