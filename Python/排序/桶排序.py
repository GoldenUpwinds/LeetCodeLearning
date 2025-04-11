import os

path = os.path.join(".", "Python", "排序", "input.txt")
file = open(path)
nums = list(map(int, file.readline().split()))
file.close()
gt = sorted(nums)


class Solution:
    def sortMethod(self, nums):
        max_bucket = max(nums)
        buckets = [[] for _ in range(10)]
        bucket_cut = max_bucket // 10 + 1

        for num in nums:
            buckets[num // bucket_cut].append(num)

        for bucket in buckets:
            bucket.sort()

        i = 0

        for bucket in buckets:
            for num in bucket:
                nums[i] = num
                i += 1
        return nums


Solve = Solution()
output = Solve.sortMethod(nums)
print(output == gt)
