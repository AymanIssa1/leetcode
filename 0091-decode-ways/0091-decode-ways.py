class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s and s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[-1] = 1 
        dp[len(s) - 1] = 1 if s[-1] != '0' else 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

                if int(s[i:i+2]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]