from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        sequence = []

        def trackback(startIndex):
            output.append(sequence[:])
            if startIndex == len(nums):
                return
            
            for i in range(startIndex,len(nums)):
                sequence.append(nums[i])
                trackback(i+1)
                sequence.pop()
            return

        trackback(0)
        return output

Solve = Solution()   
nums = [1,2,3]
print(Solve.subsets(nums))

