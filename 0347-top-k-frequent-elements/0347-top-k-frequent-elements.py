class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = {}
        heap = []

        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        for num in freqs.keys():
            heappush(heap, (-freqs[num], num))
        
        top_k = []
        for _ in range(k):
            freq, num = heappop(heap)
            top_k.append(num)

        return top_k