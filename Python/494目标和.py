class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum_nums = sum(nums)
        if sum_nums < abs(target):
            return 0
        if (sum_nums+target) % 2 == 1:
            return 0
        target_bag = (target + sum_nums) // 2
        dp = [0] * (target_bag + 1)
        dp[0] = 1

        for i in range(len(nums)):
            for j in range(target_bag,nums[i]-1,-1):
                dp[j] += dp[j-nums[i]]
        
        return dp[-1]
    
Solve = Solution()
nums = [1,1,1,1,1]
target = 3
print(Solve.findTargetSumWays(nums,target))