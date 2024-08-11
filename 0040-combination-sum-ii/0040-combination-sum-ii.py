class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) < target:
            return []
        candidates.sort()
        result = []
        self.helper(0, candidates, target, [], result)
        return result

    def helper(self, index, candidates, target, curr_subset, result):
        if sum(curr_subset) == target:
            if sorted(curr_subset) not in result:
                result.append(curr_subset)
            return

        if index >= len(candidates) or sum(curr_subset) > target:
            return

        for i in range(index, len(candidates)):
            self.helper(i + 1, candidates, target, curr_subset + [candidates[i]], result)
