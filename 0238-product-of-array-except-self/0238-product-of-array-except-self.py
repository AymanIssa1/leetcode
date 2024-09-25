class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
        if zeros > 1:
            return [0] * n
        
        output = [0] * n 
        total_product = 1

        for num in nums:
            if num != 0:
                total_product *= num
        print(total_product)
        for i in range(n):
            print(i)
            if zeros == 1 and nums[i] != 0:
                output[i] = 0
            elif zeros == 1 and nums[i] == 0:
                output[i] = total_product
            else:
                output[i] = total_product / nums[i]
        
        return output