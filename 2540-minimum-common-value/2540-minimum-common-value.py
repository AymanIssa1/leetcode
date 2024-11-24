class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        num1_index = 0
        num2_index = 0

        while num1_index < len(nums1) and num2_index < len(nums2):
            if nums1[num1_index] < nums2[num2_index]:
                num1_index += 1
            elif nums1[num1_index] > nums2[num2_index]:
                num2_index += 1
            else:
                return nums1[num1_index]
        
        return -1