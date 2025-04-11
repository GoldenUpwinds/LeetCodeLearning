import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)


class Solution:
    def partition(self, nums, left, right):
        i, j = left, right
        while i < j:
            while i < j and nums[left] <= nums[j]:
                j -= 1
            while i < j and nums[left] >= nums[i]:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        return i

    def sortMethod(self, nums):
        def quicksort(left, right):
            if left >= right:
                return
            dummy = self.partition(nums, left, right)
            quicksort(left, dummy - 1)
            quicksort(dummy + 1, right)
            return

        quicksort(0, len(nums) - 1)
        return nums


Solve = Solution()
output = Solve.sortMethod(nums)
print(output == gt)
