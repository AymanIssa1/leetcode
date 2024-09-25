class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        output = 0

        for num in nums:
            if num - 1 not in nums:
                curr_counter = 1
                curr_num = num + 1  
                
                while curr_num in nums:
                    curr_counter += 1
                    curr_num += 1

                output = max(output, curr_counter)

        return output
