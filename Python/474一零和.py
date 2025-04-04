class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(m+1)]

        for s in strs:
            zeros, ones = 0, 0
            for char in s:
                if char == '0':
                    zeros += 1
                else:
                    ones += 1
            
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zeros][j-ones]+1)
            
        return dp[-1][-1]

Solve = Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(Solve.findMaxForm(strs,m,n))