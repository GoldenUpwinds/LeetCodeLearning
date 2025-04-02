from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost)+1)
        cost.append(0)
        if len(cost) <= 2:
            return 0

        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return dp[-1]


Solve = Solution()
cost = [10, 15, 20]
print(Solve.minCostClimbingStairs(cost))
