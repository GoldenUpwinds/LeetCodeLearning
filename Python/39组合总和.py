from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = []
        output = []

        def trackback(start_index, target):
            if target == 0:
                output.append(nums[:])
                return
            
            for i in range(start_index,len(candidates)):
                num = candidates[i]
                if target < num:
                    break

                nums.append(num)
                trackback(i,target-num)
                nums.pop()
            
            return
        
        trackback(0, target)

        return output

Solve = Solution()
candidates = [2,3,6,7]
target = 7
print(Solve.combinationSum(candidates,target))