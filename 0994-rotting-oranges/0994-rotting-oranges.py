class Solution(object):
    def orangesRotting(self, grid):
        min_minutes = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0

        while queue:
            min_minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for direction_row, direction_col in directions:
                    next_row, next_col = r + direction_row, c + direction_col
                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        queue.append((next_row, next_col))
                        fresh_oranges -= 1
                    
            # if all fresh oranges are rooted, return the time taken
            if fresh_oranges == 0:
                return min_minutes

        return -1