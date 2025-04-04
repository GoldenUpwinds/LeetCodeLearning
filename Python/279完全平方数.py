class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        index = 1
        while index * index <= n:
            for i in range(index*index,len(dp)):
                dp[i] = min(dp[i],dp[i-index*index]+1)
            index += 1
        
        return dp[-1]

Solve = Solution()
n = 12
print(Solve.numSquares(n))