class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = [[0] * (2*k+1) for _ in range(len(prices))]

        for i in range(2*k+1):
            if i % 2 == 1:
                dp[0][i] = -prices[0]
        
        for i in range(1,len(prices)):
            for j in range(1,2*k+1):
                if j % 2 == 1:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+prices[i])
        
        return dp[-1][-1]

Solve = Solution()
k = 2
prices = [2,4,1]
print(Solve.maxProfit(k,prices))