class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(0, candidates, target, [], result)
        return result

    def helper(self, index, candidates, target, curr_subset, result):
        print("index=",index,", curr_subset=", curr_subset)
        if sum(curr_subset) == target:
            result.append(curr_subset)
            return

        if index >= len(candidates) or sum(curr_subset) > target:
            return

        self.helper(index, candidates, target, curr_subset + [candidates[index]], result)
        self.helper(index + 1, candidates, target, curr_subset, result)
