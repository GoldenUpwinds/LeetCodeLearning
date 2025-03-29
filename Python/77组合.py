from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        ans = []

        def helper(start_num,n,k):
            if len(nums) == k:
                ans.append(nums[:])
                return

            for i in range(start_num,n-(k-len(nums))+2):
                nums.append(i)

                if i <= n:
                    helper(i+1,n,k)
                
                nums.pop()
            return
        
        helper(1,n,k)
        return ans

Solve = Solution()
n = 4
k = 2
print(Solve.combine(n,k))