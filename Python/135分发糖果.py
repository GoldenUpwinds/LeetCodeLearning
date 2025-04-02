from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys = [1] * len(ratings)

        for index in range(len(ratings) - 1):
            if ratings[index] < ratings[index + 1]:
                candys[index + 1] = max(candys[index + 1], 1 + candys[index])

        for index in range(len(ratings) - 1, 0, -1):
            if ratings[index] < ratings[index - 1]:
                candys[index - 1] = max(candys[index - 1], 1 + candys[index])

        return sum(candys)


Solve = Solution()
ratings = [1, 0, 2]
print(Solve.candy(ratings))
