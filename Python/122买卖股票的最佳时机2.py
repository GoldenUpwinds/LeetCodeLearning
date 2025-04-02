from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0

        for index in range(1, len(prices)):
            own = prices[index] - prices[index - 1]
            if own > 0:
                output += own

        return output


Solve = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(Solve.maxProfit(prices))
