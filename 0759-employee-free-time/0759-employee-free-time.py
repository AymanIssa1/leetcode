"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)
        
        intervals.sort(key=lambda x: (x.start, x.end))

        merged_intervals = []
        merged_intervals.append(intervals[0])

        for i in range(1, len(intervals)):
            prev = merged_intervals[-1]
            curr = intervals[i]
            
            if curr.start <= prev.end:
                merged_intervals[-1].start = min(prev.start, curr.start)
                merged_intervals[-1].end = max(prev.end, curr.end)
            else:
                merged_intervals.append(intervals[i])
        
        free_intervals = []
        for i in range(1, len(merged_intervals)):
            prev = merged_intervals[i-1]
            curr = merged_intervals[i]

            if prev.end < curr.start:
                free_intervals.append(Interval(prev.end, curr.start)) 
        
        return free_intervals
        