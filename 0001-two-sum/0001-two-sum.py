class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()
        for i in range(len(nums)):
            remaining_num = target - nums[i]
            if remaining_num in hashmap:
                return [hashmap[remaining_num], i]
            else:
                hashmap[nums[i]] = i
        
        return []
