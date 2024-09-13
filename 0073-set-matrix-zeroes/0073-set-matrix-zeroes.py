class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeros.append((r, c))
        
        for r, c in zeros:
            for i in range(len(matrix)):
                matrix[i][c] = 0
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
