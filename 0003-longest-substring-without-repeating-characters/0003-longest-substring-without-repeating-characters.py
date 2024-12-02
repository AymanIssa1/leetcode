class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}
        start = 0
        max_len = 0
        for end in range(len(s)):
            if s[end] in memo:
                start = max(start, memo[s[end]] + 1)
            max_len = max(max_len, (end - start + 1))
            memo[s[end]] = end

        return max_len
        