class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        output = [[],[]]

        for num in nums1:
            if num not in nums2 and num not in output[0]:
                output[0].append(num)
        
        for num in nums2:
            if num not in nums1 and num not in output[1]:
                output[1].append(num)

        return output