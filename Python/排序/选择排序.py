import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)


class Solution:
    def sortMethod(self, nums):
        for i in range(len(nums) - 1):
            min_val = (i, nums[i])
            for j in range(i, len(nums)):
                if nums[j] < min_val[1]:
                    min_val = (j, nums[j])
            nums[i], nums[min_val[0]] = min_val[1], nums[i]
        return nums


Solve = Solution()
print(Solve.sortMethod(nums) == gt)
