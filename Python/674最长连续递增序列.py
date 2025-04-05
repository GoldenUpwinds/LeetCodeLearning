class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        dp = [1] * len(nums)

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            if dp[i] > result:
                result = dp[i]
        
        return result

Solve = Solution()
nums = [1,3,5,4,7]
print(Solve.findLengthOfLCIS(nums))