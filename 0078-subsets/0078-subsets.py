class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        subsets.append([])

        for num in nums:
            for i in range(len(subsets)):
                set1 = list(subsets[i])
                set1.append(num)
                subsets.append(set1)

        return subsets