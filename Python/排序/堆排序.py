import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)


import heapq


class Solution:
    def sortMethod(self, nums):
        heapq.heapify(nums)
        output = []

        while nums:
            output.append(heapq.heappop(nums))

        return output


Solve = Solution()
output = Solve.sortMethod(nums)
print(output == gt)
