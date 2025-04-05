class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        elif len(s) == 1:
            return 1
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 1

        dp[-1][-1] = True

        for i in range(len(dp)-2,-1,-1):
            for j in range(i,len(dp)):
                if s[i] == s[j]:
                    if i == j:
                        dp[i][j] = True
                        result += 1
                    elif j-i == 1:
                        dp[i][j] = True
                        result += 1
                    elif j>0 and dp[i+1][j-1] == True:
                        dp[i][j] = True
                        result += 1
        return result

Solve = Solution()
s = "abc"
print(Solve.countSubstrings(s))