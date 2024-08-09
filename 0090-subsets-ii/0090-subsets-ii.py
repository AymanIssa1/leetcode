class Solution(object):
    def subsetsWithDup(self, nums):
        subsets = []
        currSet = []
        nums.sort()
        self.helper(0, nums, currSet, subsets)
        return subsets

    def helper(self, i, nums, currSet, subsets):
        if i >= len(nums):
            subsets.append(currSet[:])
            return
            
        currSet.append(nums[i])
        self.helper(i+1, nums, currSet, subsets)

        currSet.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i+1, nums, currSet, subsets)

        
