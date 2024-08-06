class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left, right = 0, len(height) - 1

        while left < right:
            diff = right - left
            min_height = min(height[right], height[left])
            max_water = max(max_water, diff * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
            