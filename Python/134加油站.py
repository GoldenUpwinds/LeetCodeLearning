from typing import List


# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         curSum, minOil = 0, float("inf")

#         for i in range(len(gas)):
#             curSum += gas[i] - cost[i]
#             if curSum < minOil:
#                 minOil = curSum

#         if curSum < 0:
#             return -1
#         if minOil >= 0:
#             return 0

#         for i in range(len(gas) - 1, -1, -1):
#             rest = gas[i] - cost[i]
#             minOil += rest
#             if minOil >= 0:
#                 return i
#         return -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum, totalSum = 0, 0
        startIndex = 0

        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]

            if curSum < 0:
                startIndex = i + 1
                curSum = 0

        if totalSum < 0:
            return -1
        else:
            return startIndex


Solve = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(Solve.canCompleteCircuit(gas, cost))
