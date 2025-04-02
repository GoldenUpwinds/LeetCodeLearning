from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                cash[bill] += 1
            elif bill == 10:
                if cash[5] > 0:
                    cash[5] -= 1
                    cash[10] += 1
                else:
                    return False
            elif bill == 20:
                if cash[10] > 0 and cash[5] > 0:
                    cash[10], cash[5] = cash[10] - 1, cash[5] - 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                else:
                    return False
        return True


Solve = Solution()
bills = [5, 5, 5, 10, 20]
print(Solve.lemonadeChange(bills))
