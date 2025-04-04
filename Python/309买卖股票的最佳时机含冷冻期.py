class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0]*4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i],dp[i-1][3]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        
        return max(dp[-1][1:])

Solve = Solution()
prices = [1,2,3,0,2]
print(Solve.maxProfit(prices))