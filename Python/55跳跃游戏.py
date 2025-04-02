from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = 0

        for index in range(len(nums)):
            if canReach < index:
                return False
            canReach = max(index + nums[index], canReach)
        return True


Solve = Solution()
nums = [3, 2, 1, 0, 4]
print(Solve.canJump(nums))
