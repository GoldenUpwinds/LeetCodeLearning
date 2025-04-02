from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        curDim, preDim = 0, 0
        output = 1

        for index in range(len(nums) - 1):
            curDim = nums[index + 1] - nums[index]
            if (curDim > 0 and preDim <= 0) or (curDim < 0 and preDim >= 0):
                output += 1
                preDim = curDim
        return output


Solve = Solution()
nums = [1, 7, 4, 9, 2, 5]
print(Solve.wiggleMaxLength(nums))
