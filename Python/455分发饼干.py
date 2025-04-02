from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        output = 0
        s.sort()
        s.reverse()
        g.sort()
        g.reverse()

        Index = 0

        for child in g:
            if Index == len(s):
                break
            if s[Index] >= child:
                output += 1
                Index += 1
        return output


Solve = Solution()
g = [1, 2, 3]
s = [1, 1]
print(Solve.findContentChildren(g, s))
