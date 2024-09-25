class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        output = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num
                counter = 1

                while curr + 1 in nums_set:
                    curr += 1
                    counter += 1
                
                output = max(output, counter)


        return output
        