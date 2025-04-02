class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)

        return dp[-1]


Solve = Solution()
n = 10
print(Solve.integerBreak(n))
