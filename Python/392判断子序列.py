class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp = [[0]*(len(t) + 1) for _ in range(len(s)+1)]
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[-1][-1] == len(s)

Solve = Solution()
s = "abc"
t = "ahbgdc"
print(Solve.isSubsequence(s,t))