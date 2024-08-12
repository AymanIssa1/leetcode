class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n in [1,2]:
            return 1
        
        n1, n2, n3 = 0, 1, 1
        
        for i in range(2, n):
            n1, n2, n3 = n2, n3, n1+n2+n3
        
        return n3