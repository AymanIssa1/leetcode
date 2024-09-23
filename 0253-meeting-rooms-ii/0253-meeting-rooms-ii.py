class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        start_times = sorted(interval[0] for interval in intervals)
        end_times = sorted(interval[1] for interval in intervals)

        start_index, end_index = 0, 0
        used_rooms = 0
        max_rooms = 0

        while start_index < len(intervals):
            if start_times[start_index] < end_times[end_index]:
                used_rooms += 1
                start_index += 1
            else:
                used_rooms -= 1
                end_index += 1

            max_rooms = max(max_rooms, used_rooms)
        
        return max_rooms
        