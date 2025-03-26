from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_left[0] = height[0]
        max_right[len(height)-1] = height[len(height)-1]

        for i in range(1,len(height)):
            max_left[i]=max(height[i],max_left[i-1])
        for i in range(len(height)-2,-1,-1):
            max_right[i]=max(height[i],max_right[i+1])
        aux = 0
        for i in range(len(height)):
            count = max(0, min(max_left[i],max_right[i])-height[i])
            aux += count
        return aux

Solve = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solve.trap(height))