import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)


class Solution:
    def sortMethod(self, nums):
        for i in range(1, len(nums)):
            base = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > base:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = base
        return nums


Solve = Solution()
output = Solve.sortMethod(nums)
print(output == gt)
