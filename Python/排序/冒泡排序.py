import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)


class Solution:
    def sortMethod(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            flag = False
            for j in range(0, i):
                if nums[j + 1] < nums[j]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
                    flag = True
            if not flag:
                return nums
        return nums


Solve = Solution()
output = Solve.sortMethod(nums)
print(output == gt)
