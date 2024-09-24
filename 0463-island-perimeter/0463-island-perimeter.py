class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        output = [0]
        self.helper(grid, 0, 0, None, None, visited, output)
        return output[0]

    def helper(self, grid, row, col, prev_row, prev_col, visited, output):
        if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
            return
        
        if (row, col) in visited:
            return

        visited.add((row, col))

        if grid[row][col] == 1:
            output[0] += 4

            if 0 <= row -1 < len(grid) and grid[row - 1][col]:
                output[0] -= 1
            if 0 <= row + 1 < len(grid) and grid[row + 1][col]:
                output[0] -= 1
            if 0 <= col - 1 < len(grid[0]) and grid[row][col - 1]:
                output[0] -= 1
            if 0 <= col + 1 < len(grid[0]) and grid[row][col + 1]:
                output[0] -= 1

        self.helper(grid, row + 1, col, row, col, visited, output)
        self.helper(grid, row - 1, col, row, col, visited, output)
        self.helper(grid, row, col + 1, row, col, visited, output)
        self.helper(grid, row, col - 1, row, col, visited, output)

    