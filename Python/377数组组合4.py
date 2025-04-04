class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(0,len(dp)):
            for j in range(0,len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]]
        
        return dp[-1]

Solve = Solution()
nums = [1,2]
target = 10
print(Solve.combinationSum4(nums,target))