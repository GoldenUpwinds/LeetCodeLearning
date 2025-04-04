class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(0,len(dp)):
            for word in wordDict:
                if i < len(word):
                    continue
                if word == s[i-len(word):i] and dp[i-len(word)]:
                    dp[i] = True
        
        return dp[-1]

Solve = Solution()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(Solve.wordBreak(s,wordDict))