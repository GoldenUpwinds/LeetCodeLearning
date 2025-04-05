class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0] * (len(word2)+1) for _ in range((len(word1))+1)]

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return len(word1) + len(word2) - 2 * dp[-1][-1]

Solve = Solution()
word1 = "sea"
word2 = "eat"
print(Solve.minDistance(word1,word2))