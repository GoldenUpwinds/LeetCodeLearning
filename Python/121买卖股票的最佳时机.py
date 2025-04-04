class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('inf')
        own = 0
        for price in prices:
            if price < buy:
                buy = price
            own = max(0,price-buy,own)
        return own

Solve = Solution()
prices = [7,1,5,3,6,4]
print(Solve.maxProfit(prices))