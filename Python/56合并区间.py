from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        output = []

        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])

        return output


Solve = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(Solve.merge(intervals))
