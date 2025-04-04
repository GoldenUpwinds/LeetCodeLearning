class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0],dp[0][1] = -prices[0], 0

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)

        return max(dp[-1])
    
Solve = Solution()
prices = [9,8,7,1,2]
fee = 3
print(Solve.maxProfit(prices,fee))