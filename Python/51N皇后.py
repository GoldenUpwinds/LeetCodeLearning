from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        table = [['.'] * n for _ in range(n)]

        def isValid(n,row,col):
            for i in range(row):
                if table[i][col] == 'Q':
                    return False
            
            for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
                if table[i][j] == 'Q':
                    return False
            
            for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
                if table[i][j] == 'Q':
                    return False
            
            return True

        def trackback(layer,n):
            if layer == n:
                output.append(["".join(row) for row in table])
                return
            
            for i in range(n):
                table[layer][i] = 'Q'
                if isValid(n,layer,i):
                    trackback(layer+1,n)
                table[layer][i] = '.'
            
            return
        
        trackback(0,n)
        return output

Solve = Solution()
n = 4
print(Solve.solveNQueens(n))
            