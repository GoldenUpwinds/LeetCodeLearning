from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        sequence = []
        used = [False] * len(nums)

        def trackback():
            if len(sequence) == len(nums):
                output.append(sequence[:])
                return

            layer_used = set()
            for i in range(len(nums)):
                if used[i] or nums[i] in layer_used:
                    continue
                
                layer_used.add(nums[i])
                used[i] = True
                sequence.append(nums[i])
                trackback()
                sequence.pop()
                used[i] = False
            return
        
        trackback()
        return output

Solve = Solution()
nums = [1,1,2]
print(Solve.permuteUnique(nums))


