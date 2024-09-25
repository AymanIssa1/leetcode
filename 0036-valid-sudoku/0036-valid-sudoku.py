class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        digits = {}
        for digit in range(1,10):
            digits[str(digit)] = 1
        
        # Check rows
        for row in range(9):
            curr_digits = digits.copy()
            for col in range(9):
                digit = board[row][col]
                if digit == ".":
                    continue
                if curr_digits[digit] <= 0:
                    return False
                curr_digits[digit] -= 1
        
        # Check rows
        for col in range(9):
            curr_digits = digits.copy()
            for row in range(9):
                digit = board[row][col]
                if digit == ".":
                    continue
                if curr_digits[digit] <= 0:
                    return False
                curr_digits[digit] -= 1

        # Check Squares
        for box_row in range(0,3):
            for box_col in range(0,3):
                curr_digits = digits.copy()
                for row in range(box_row * 3, (box_row * 3) + 3):
                    for col in range(box_col * 3, (box_col * 3) + 3):
                        digit = board[row][col]
                        if digit == ".":
                            continue
                        if curr_digits[digit] <= 0:
                            return False
                        curr_digits[digit] -= 1

        return True