import heapq
import sys
import ast

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-x for x in nums]
        heapq.heapify(nums)
        Index = 1
        while Index < k:
            heapq.heappop(nums)
            Index += 1
        return -nums[0]

def main():
    input_all = sys.stdin.readlines()
    nums = ast.literal_eval(input_all[0].strip())
    k = int(input_all[1].strip())

    Solve = Solution()
    print(Solve.findKthLargest(nums,k))

if __name__ == "__main__":
    main()
