from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        curDistance = 0
        output = 0
        nextDistance = 0

        for i in range(len(nums)):
            nextDistance = max(nextDistance, i + nums[i])

            if curDistance < len(nums) - 1:
                if curDistance == i:
                    output += 1
                    curDistance = nextDistance
            else:
                break
        return output


Solve = Solution()
nums = [2, 3, 1, 1, 4]
print(Solve.jump(nums))
