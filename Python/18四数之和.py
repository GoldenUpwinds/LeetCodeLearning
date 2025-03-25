from typing import List

class Solution:
    def fourSum(self, nums, target):
        output = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                absum = nums[i] + nums[j]
                if nums[j] == nums[j-1] and j > i+1:
                    continue
                left, right = j+1, len(nums)-1
                while left<right:
                    sumall = nums[left] + nums[right] + absum
                    if sumall > target:
                        right -= 1
                    elif sumall < target:
                        left += 1
                    else:
                        output.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left] == nums[left+1]:
                            left += 1
                        while left<right and nums[right] == nums[right-1]:
                            right -= 1
                        left, right = left+1, right-1
        return output

Solve = Solution()
nums = [-3,-2,-1,0,0,1,2,3]
target = 0
print(Solve.fourSum(nums=nums,target=target))