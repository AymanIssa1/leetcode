class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.prefix_sum = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix_sum.append(curr_sum)


        # [1, 2, 3, 4]
        # [1, 3, 6, 10]
        # [0.1, 0.3, 0.6 1.0]

        # [1, 2, 1, 1]
        # [1, 3, 4, 5]

        # Binary Search
        

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.random() * self.total_sum
        
        start, end = 0, len(self.prefix_sum) - 1
        while start < end:
            mid = (start + end) // 2
            if target > self.prefix_sum[mid]:
                start = mid + 1
            else:
                end = mid 

        return start


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()