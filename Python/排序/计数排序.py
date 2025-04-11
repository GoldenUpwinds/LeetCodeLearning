import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)

import collections


class Solution:
    def sortMethod(self, nums):
        hash_counters = collections.Counter(nums)
        hash_counters = collections.OrderedDict(sorted(hash_counters.items()))
        i = 0
        for counter in hash_counters.items():
            key, value = counter
            nums[i:i+value] = [key] * value
            i += value
        return nums


Solve = Solution()
output = Solve.sortMethod(nums)
print(output == gt)
