class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left,right = 0,len(nums)-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

Solve = Solution()
nums = [3,1]
target = 1
print(Solve.search(nums,target))
