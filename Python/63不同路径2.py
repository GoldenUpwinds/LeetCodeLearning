from typing import List


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         dp = [[0] * n for _ in range(m)]
#         if obstacleGrid[0][0] == 0:
#             dp[0][0] = 1

#         for i in range(1, m):
#             if obstacleGrid[i][0] == 1:
#                 dp[i][0] = 0
#             else:
#                 dp[i][0] = dp[i - 1][0]

#         for j in range(1, n):
#             if obstacleGrid[0][j] == 1:
#                 dp[0][j] = 0
#             else:
#                 dp[0][j] = dp[0][j - 1]

#         for i in range(1, m):
#             for j in range(1, n):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

#         return dp[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        if obstacleGrid[0][0] == 0:
            dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]


Solve = Solution()
obstacleGrid = [[0, 1]]
print(Solve.uniquePathsWithObstacles(obstacleGrid))
