class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        dp = [[0] * (len(nums1) + 1) for _ in range(len(nums2) + 1)]
        output = 0

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if nums2[i-1] == nums1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > output:
                    output = dp[i][j]
        return output

Solve = Solution()
nums1 = [1,1,0,0,1,1]
nums2 = [0,0]
print(Solve.findLength(nums1,nums2))