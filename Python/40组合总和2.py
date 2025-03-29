from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = []
        output = []

        def trackback(start_index, target):
            if target == 0:
                output.append(nums[:])
                return
            
            for i in range(start_index,len(candidates)):
                num = candidates[i]
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue
                if target < num:
                    break

                nums.append(num)
                trackback(i+1,target-num)
                nums.pop()
            
            return
        
        trackback(0, target)

        return output

Solve = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(Solve.combinationSum2(candidates,target))