class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        output = 0

        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start < last_end:
                output += 1
            else:
                last_end = curr_end
        
        return output