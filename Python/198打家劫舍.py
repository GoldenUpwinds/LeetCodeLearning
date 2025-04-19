from typing import List
import ast
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxF, minF, output = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            max_now, minNow = maxF, minF
            maxF = max(max_now*num,minNow*num,num)
            minF = min(max_now*num,minNow*num,num)
            if maxF > output:
                output = maxF
        return output


def main():
    nums = ast.literal_eval(sys.stdin.read().strip())
    Solve = Solution()
    print(Solve.maxProduct(nums))

if __name__ == "__main__":
    main()
