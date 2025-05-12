class Solution(object):
    def exist(self, board, word):
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.word_search_rec(board, word, 0, x, y):
                    return True
        return False


    def word_search_rec(self, board, word, word_index, x, y):
        if word_index == len(word):
            return True
        x_len, y_len = len(board), len(board[0])

        if not (0 <= x < x_len and 0 <= y < y_len):
            return False
        if board[x][y] != word[word_index]:
            return False

        # mark the cell as visited
        temp = board[x][y]
        board[x][y] = "#"

        left = self.word_search_rec(board, word, word_index + 1, x - 1, y)
        right = self.word_search_rec(board, word, word_index + 1, x + 1, y)
        top = self.word_search_rec(board, word, word_index + 1, x, y - 1)
        bottom = self.word_search_rec(board, word, word_index + 1, x, y + 1)

        if left or right or top or bottom:
            return True

        board[x][y] = temp

        return False
