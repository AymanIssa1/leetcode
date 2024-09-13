class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []

        for row in range(numRows):
            if row == 0:
                output.append([1])
            else:
                curr_row = [1]
                for i in range(1, row):
                    val = output[row-1][i-1] + output[row-1][i]
                    curr_row.append(val)
                
                curr_row.append(1)
                output.append(curr_row)
        
        return output
                        