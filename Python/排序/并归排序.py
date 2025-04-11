import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)


class Solution:
    def merge(self, nums, left, right):
        tmp = []
        middle = (left + right) // 2
        i, j = left, middle + 1

        while i <= middle and j <= right:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1

        while i <= middle:
            tmp.append(nums[i])
            i += 1
        while j <= right:
            tmp.append(nums[j])
            j += 1

        nums[left: right + 1] = tmp[:]
        return

    def sortMethod(self, nums):
        def merge_sort(left, right):
            if left >= right:
                return

            middle = (left + right) // 2
            merge_sort(left, middle)
            merge_sort(middle + 1, right)

            self.merge(nums, left, right)
            return
        merge_sort(0,len(nums)-1)
        return nums


Solve = Solution()
output = Solve.sortMethod(nums)
print(output == gt)
