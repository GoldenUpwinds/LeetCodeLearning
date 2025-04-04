class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin,len(dp)):
                dp[i] = min(dp[i],dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            dp[-1] = -1
        return dp[-1]

Solve = Solution()
coins = [1, 2, 5]
amount = 11
print(Solve.coinChange(coins,amount))