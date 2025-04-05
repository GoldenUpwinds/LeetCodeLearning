class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

Solve = Solution()
nums1 = [1,4,2]
nums2 = [1,2,4]
print(Solve.maxUncrossedLines(nums1,nums2))