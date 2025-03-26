from typing import List
import heapq, collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appear_times = collections.Counter(nums)
        top_heapq = [(v,k) for k,v in appear_times.items()]
        heapq.heapify(top_heapq)

        while len(top_heapq) > k:
            heapq.heappop(top_heapq)
        output = [None] * k
        for Index in range(k):
            output[Index] = top_heapq[Index][1]
        return output

Solve = Solution()
nums = [1,1,1,2,2,3] 
k = 2
print(Solve.topKFrequent(nums,k))
