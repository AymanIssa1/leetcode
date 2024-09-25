class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [0] * n
        all_product = 1
        zeros_count = 0

        for num in nums:
            if num == 0:
                zeros_count += 1
            else:
                all_product *= num
        
        if zeros_count > 1:
            return output

        if zeros_count == 1:
            for i in range(n):
                if nums[i] != 0:
                    continue
                output[i] = all_product
        else:
            for i in range(n):
                output[i] = all_product // nums[i]

        return output
        