class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [-1] * n
        stack = [] # to stoer indices

        for i in range(2*n):
            print(stack)
            while stack and nums[stack[-1]] < nums[i % n]:
                output[stack.pop()] = nums[i % n]

            if i < n:
                stack.append(i)

        return output