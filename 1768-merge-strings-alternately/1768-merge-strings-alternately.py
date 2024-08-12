class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        index1 = 0
        index2 = 0
        output = ""

        while index1 < len(word1) and index2 < len(word2):
            output += word1[index1]
            output += word2[index2]
            index1 += 1
            index2 += 1

        while index1 < len(word1):
            output += word1[index1]
            index1 += 1
            index2 += 1

        while index2 < len(word2):
            output += word2[index2]
            index2 += 1

        return output
