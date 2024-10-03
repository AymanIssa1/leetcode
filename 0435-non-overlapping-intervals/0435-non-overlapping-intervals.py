class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1]) 
        output = 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start < prev_end:
                output += 1
            else:
                prev_end = curr_end

        return output

# [[1,100],[11,22],[1,11],[2,12]]
# [[1, 11], [2, 12], [11, 22], [1, 100]]
