class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]

        for i in range(len(s)+1):
            dp[0][i] = 1
        
        for i in range(1,len(dp)):
            for j in range(i,len(dp[0])):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

Solve = Solution()
s = "rabbbit"
t = "rabbit"
print(Solve.numDistinct(s,t))