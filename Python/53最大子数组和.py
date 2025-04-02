from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = float("-inf")
        aus = float("-inf")

        for num in nums:
            if num > aus and aus < 0:
                aus = 0

            aus += num
            if aus > output:
                output = aus

        return output


Solve = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solve.maxSubArray(nums))
