class Solution(object):
    def merge(self, intervals):
        merged_intervals = []
        
        intervals.sort()
        
        for interval in intervals:
            if len(merged_intervals) == 0:
                merged_intervals.append(interval)
            else:
                prev_start, prev_end = merged_intervals[-1]
                curr_start, curr_end = interval
                
                if curr_start <= prev_end:
                    new_start = min(prev_start, curr_start)
                    new_end = max(prev_end, curr_end)
                    merged_intervals[-1] = [new_start, new_end]
                else:
                    merged_intervals.append(interval)
        
        return merged_intervals