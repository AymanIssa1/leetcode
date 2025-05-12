class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0 for _ in range(len(nums))]
        zeros_count = 0
        arr_product = 1

        for num in nums:
            if num != 0:
                arr_product = arr_product * num
            else:
                zeros_count += 1
        
        if zeros_count == 0:
            for i in range(len(nums)):
                result[i] = arr_product / nums[i]

        if zeros_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result[i] = arr_product


        return result