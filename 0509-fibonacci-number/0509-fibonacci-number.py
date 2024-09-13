class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n in [1,2]:
            return 1
        
        memo = [1, 1]

        for i in range(2, n ):
            memo[0], memo[1] = memo[1], memo[0] + memo[1]

        return memo[1]