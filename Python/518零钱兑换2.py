class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin,len(dp)):
                dp[i] += dp[i-coin]
        
        return dp[-1]
    
Solve = Solution()
amount = 5
coins = [1, 2, 5]
print(Solve.change(amount,coins))