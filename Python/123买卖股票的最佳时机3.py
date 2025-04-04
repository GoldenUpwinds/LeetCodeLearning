class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0] * 5 for _ in range(len(prices))]
        dp[0][1],dp[0][3] = -prices[0],-prices[0]
        
        for i in range(1,len(prices)):
            dp[i][1] = max(dp[i-1][0]-prices[i],dp[i-1][1])
            dp[i][2] = max(dp[i-1][1]+prices[i],dp[i-1][2])
            dp[i][3] = max(dp[i-1][2]-prices[i],dp[i-1][3])
            dp[i][4] = max(dp[i-1][3]+prices[i],dp[i-1][4])
        
        return dp[-1][-1]

Solve = Solution()
prices = [3,3,5,0,0,3,1,4]
print(Solve.maxProfit(prices))