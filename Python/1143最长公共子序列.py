class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

Solve = Solution()
text1 = "abcde"
text2 = "ace"
print(Solve.longestCommonSubsequence(text1,text2))