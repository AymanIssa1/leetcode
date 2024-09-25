class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freqs = {}

        for curr in strs:
            anagram = str(sorted(curr))
            if anagram not in freqs:
                freqs[anagram] = [str(curr)]
            else:
                freqs[anagram].append(str(curr))    

        return freqs.values()