class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1] * n for _ in range(m)]

        if m == 1 or n == 1:
            return 1

        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i - 1][j] + board[i][j - 1]

        return board[-1][-1]


Solve = Solution()
m = 3
n = 7
print(Solve.uniquePaths(m, n))
