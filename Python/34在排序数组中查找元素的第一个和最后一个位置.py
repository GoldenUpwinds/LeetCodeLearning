class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        i,j = 0,len(nums)-1
        get_num = None

        while i <= j:
            mid = (i+j) // 2

            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                get_num = mid
                break
        
        if get_num != None:
            left,right = get_num,get_num
            while left >= 0 and nums[left] == target:
                left -= 1
            left += 1
            while right <= len(nums)-1 and nums[right] == target:
                right += 1
            right -= 1
            return [left,right]
        return [-1,-1]

Solve = Solution()
nums = [1]
target = 1
print(Solve.searchRange(nums,target))