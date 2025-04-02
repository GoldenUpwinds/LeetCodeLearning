class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[-1]


Solve = Solution()
n = 3
print(Solve.numTrees(n))
