class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for num in nums1:
            curr_index = nums2.index(num)
            found = False
            for i in range(curr_index + 1, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    found = True
                    break
            if not found:
                result.append(-1)

        return result 
        