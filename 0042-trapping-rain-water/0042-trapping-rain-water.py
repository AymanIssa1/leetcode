class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        n = len(height)
        left_heights = [0] * n
        right_heights = [0] * n

        left_heights[0] = height[0]
        for i in range(1, n):
            left_heights[i] = max(left_heights[i-1], height[i])

        right_heights[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_heights[i] = max(right_heights[i+1], height[i])

        for i in range(1, len(height)):
            min_height = min(left_heights[i], right_heights[i])
            trapped_water = min_height - height[i]
            if trapped_water > 0:
                result += trapped_water

        return result