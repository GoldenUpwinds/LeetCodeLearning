from typing import List


# 这题要优化的，基本回溯思路会超时
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row,col,val):
            for i in range(9):
                if board[i][col] == val or board[row][i] == val:
                    return False
            
            startrow = row // 3 * 3
            startcol = col // 3 * 3

            for i in range(startrow,startrow+3):
                for j in range(startcol,startcol+3):
                    if board[i][j] == val:
                        return False
            
            return True
        
        def trackback(row,col):
            if col == 9:
                col, row = 0, row+1
                if row == 9:
                    return True

            if board[row][col] != '.':
                return trackback(row,col+1)
                
            for val in map(str, range(1,10)):
                if isValid(row,col,val):
                    board[row][col] = val

                    if trackback(row,col+1):
                        return True
                        
                    board[row][col] = '.'
            return False
        
        trackback(0,0)
        return

Solve = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solve.solveSudoku(board)
print(board)

        