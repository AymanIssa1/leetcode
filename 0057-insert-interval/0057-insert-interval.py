class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()

        output = []

        for interval in intervals:
            if len(output) == 0:
                output.append(interval)
            else:
                prev_start, prev_end = output[-1]
                curr_start, curr_end = interval

                if curr_start <= prev_end:
                    new_start = min(prev_start, curr_start)
                    new_end = max(prev_end, curr_end)
                    output[-1] = [new_start, new_end]
                else:
                    output.append(interval)
                    
        return output
                
        