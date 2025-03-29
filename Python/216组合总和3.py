from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = []
        output = []

        def helper(start_num,k,target):
            if len(nums) == k:
                if target == 0:
                    output.append(nums[:])
                return
            
            for i in range(start_num,10):
                if target < i:
                    continue
                
                nums.append(i)
                helper(i+1,k,target-i)
                nums.pop()
            
            return output

        helper(1,k,n)
        return output

Solve = Solution()
k = 3
n = 7
print(Solve.combinationSum3(k,n))
                
