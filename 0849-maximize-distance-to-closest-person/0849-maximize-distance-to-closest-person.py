class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        left_distance = [0] * n
        right_distance = [0] * n

        distance = 0
        for i in range(n):
            if seats[i] == 1:
                distance = 0
            else:
                distance += 1
                left_distance[i] = distance
        
        distance = 0
        for i in range(n-1,-1,-1):
            if seats[i] == 1:
                distance = 0
            else:
                distance += 1
                right_distance[i] = distance

        max_middle_distance = 0
        for i in range(n):
            max_middle_distance = max(max_middle_distance, min(left_distance[i], right_distance[i]))

        return max(max_middle_distance, left_distance[0], left_distance[-1], right_distance[0], right_distance[-1])
        

