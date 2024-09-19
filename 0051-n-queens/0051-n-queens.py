class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for _ in range(n)] for _ in range(n)]
        output = []

        self.helper(board, output, 0, n)
        return output
    
    def helper(self, board, output, row, n):
        if row == n:
            output.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if self.isSafe(board, row, col):
                board[row][col] = 'Q'
                self.helper(board, output, row + 1, n)
                board[row][col] = '.'


    def isSafe(self, board, r, c):
        n = len(board)
        for i in range(n):
            if i != c and board[r][i] == 'Q':  # Check row
                return False
            if i != r and board[i][c] == 'Q':  # Check column
                return False
            # Check diagonals
            if (r + i < n and c + i < n and board[r + i][c + i] == 'Q') or \
            (r - i >= 0 and c - i >= 0 and board[r - i][c - i] == 'Q') or \
            (r + i < n and c - i >= 0 and board[r + i][c - i] == 'Q') or \
            (r - i >= 0 and c + i < n and board[r - i][c + i] == 'Q'):    
                return False
        
        # If no other queens attack, return True
        return True
        

        