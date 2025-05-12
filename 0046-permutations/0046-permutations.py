class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsLength = len(nums)
        result = []
        permutations = deque()
        permutations.append([])

        for currNum in nums:
            n = len(permutations)
            for _ in range(n):
                oldPermutation = permutations.popleft()
                for j in range(len(oldPermutation) + 1):
                    newPermutation = list(oldPermutation)
                    newPermutation.insert(j, currNum)
                    if len(newPermutation) == numsLength:
                        result.append(newPermutation)
                    else:
                        permutations.append(newPermutation)
            print(permutations)

        return result