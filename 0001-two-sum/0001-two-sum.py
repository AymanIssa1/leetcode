class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}

        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in hash_map:
                return [i, hash_map[diff]]
            else:
                hash_map[curr] = i
    