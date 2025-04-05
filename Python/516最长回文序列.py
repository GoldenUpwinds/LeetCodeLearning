class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(dp)):
            dp[i][i] = 1

        for i in range(len(dp)-2,-1,-1):
            for j in range(i+1,len(dp)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        
        return dp[0][-1]

Solve = Solution()
s = "bbbab"
print(Solve.longestPalindromeSubseq(s))