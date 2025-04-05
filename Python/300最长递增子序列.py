class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        output = 1

        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            if dp[i] > output:
                output = dp[i]
        
        return output

Solve = Solution()
nums = [0,1,0,3,2,3]
print(Solve.lengthOfLIS(nums))