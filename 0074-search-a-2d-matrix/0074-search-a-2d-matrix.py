class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        columns = len(matrix[0])

        left, right = 0, (rows * columns) - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // columns 
            c = mid % columns
            curr = matrix[r][c]

            if curr == target:
                return True
            elif curr > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

