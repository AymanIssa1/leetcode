class Solution(object):
    def subsets(self, nums):
        subsets = []
        currSet = []
        self.helper(0, nums, currSet, subsets)
        return subsets

    def helper(self, i, nums, currSet, subsets):
        if i >= len(nums):
            subsets.append(currSet[:])
            return
        
        currSet.append(nums[i])
        self.helper(i+1, nums, currSet, subsets)

        currSet.pop()
        self.helper(i+1, nums, currSet, subsets)