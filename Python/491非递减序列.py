from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = []
        sequence = []

        def trackback(startIndex=0):
            if len(sequence) >= 2:
                output.append(sequence[:])

            if startIndex == len(nums):
                return
            
            used = set()
            for i in range(startIndex,len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                if sequence and nums[i] < sequence[-1]:
                    continue
                sequence.append(nums[i])
                trackback(i+1)
                sequence.pop()
            
            return
        
        trackback()
        return output

Solve = Solution()
nums = [4,6,7,7]
print(Solve.findSubsequences(nums))