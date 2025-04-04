class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2

        dp = [0] * (target+1)
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = max(dp[j],dp[j-nums[i]]+nums[i])
        
        if dp[target] == target:
            return True
        else:
            return False

Solve = Solution()
nums = [1,5,11,5]
print(Solve.canPartition(nums))
