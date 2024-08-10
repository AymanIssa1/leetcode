class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        for num in nums:
            max_or |= num

        output = [0]
        self.helper(nums, 0, 0, max_or, output)   
        return output[0]

    def helper(self, nums, curr_or, index, max_or, output):
        if index >= len(nums):
            if curr_or == max_or:
                output[0] += 1
            return

        
        # Include the current number in the OR calculation
        self.helper(nums, curr_or | nums[index], index + 1, max_or, output)

        # Exclude the current number and move to the next
        self.helper(nums, curr_or, index + 1, max_or, output)        