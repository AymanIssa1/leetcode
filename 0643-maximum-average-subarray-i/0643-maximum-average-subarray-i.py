class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[0:k])
        output = curr_sum / float(k)

        for i in range(k, len(nums)):
            curr_sum -= nums[i-k]
            curr_sum += nums[i]

            curr_max = curr_sum / float(k)
            output = max(output, curr_max)
        
        return output
        