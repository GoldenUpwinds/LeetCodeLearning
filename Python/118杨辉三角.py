from typing import List
import sys
import math

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         output = [[1]]
#         if numRows == 1:
#             return output
#         for i in range(1,numRows):
#             lastRow = output[-1]
#             newRow = [1] * (i+1)
#             for j in range(1,len(lastRow)):
#                 newRow[j] = lastRow[j-1] + lastRow[j]
#             output.append(newRow)
#         return output

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            newRow = []
            for j in range(i+1):
                newRow.append(math.comb(i,j))
            output.append(newRow)
        return output

def main():
    numRows = int(input())
    Solve = Solution()
    print(Solve.generate(numRows))
    return

if __name__ == "__main__":
    main()
