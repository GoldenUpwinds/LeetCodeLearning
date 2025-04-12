class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0, len(nums)-1
        while True:
            middle = (left+right) // 2
            if nums[left] <= nums[right]:
                return nums[left]
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle

import ast
import sys

def main():
    nums = ast.literal_eval(sys.stdin.read())
    Solve = Solution()
    print(Solve.findMin(nums))

if __name__ == "__main__":
    main()