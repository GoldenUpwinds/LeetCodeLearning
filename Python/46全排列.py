from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sequence = []
        output = []
        used = [False] * len(nums)

        def trackback():
            if len(sequence) == len(nums):
                output.append(sequence[:])
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                sequence.append(nums[i])
                trackback()
                sequence.pop()
                used[i] = False
            
            return

        trackback()
        return output

nums = [1,2,3]
Solve = Solution()
print(Solve.permute(nums))
