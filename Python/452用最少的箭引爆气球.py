from typing import List


# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         points = sorted(points, key=lambda x: (x[0], x[1]))
#         output = 1

#         for i in range(1, len(points)):
#             if points[i][0] <= points[i - 1][1]:
#                 points[i][1] = min(points[i][1], points[i - 1][1])
#             else:
#                 output += 1
#         return output

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])

        arrow = points[0][1]
        output = 1
        


Solve = Solution()
points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
print(Solve.findMinArrowShots(points))
