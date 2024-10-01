class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row) // 2
        couples = [0] * (2 * n)
        for i in range(2 * n):
            couples[row[i]] = i
        
        swaps = 0
        for i in range(n):
            first = row[2 * i]
            second = first ^ 1  # The couple of the first person
            
            if row[2 * i + 1] != second:
                swaps += 1
                partner_index = couples[second]
                
                # Swap
                row[partner_index] = row[2 * i + 1]
                couples[row[2 * i + 1]] = partner_index
                row[2 * i + 1] = second
                couples[second] = 2 * i + 1
        
        return swaps