class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        
        output = 0
        for r in range(rows):
            for c in range(cols):
                output = max(output, self.computeLongestPath(matrix, r, c, memo, directions))

        return output

    def computeLongestPath(self, matrix, row, col, memo, directions):
        if (row, col) in memo:
            return memo[(row, col)]
                
        max_length = 1
        rows, cols = len(matrix), len(matrix[0])

        for r, c in directions:
            next_row, next_col = row + r, col + c
            if (0 <= next_row < rows) and (0 <= next_col < cols) and matrix[next_row][next_col] > matrix[row][col]:
                max_length = max(max_length, 1 + self.computeLongestPath(matrix, next_row, next_col, memo, directions))

        memo[(row, col)] = max_length
        
        return max_length
        