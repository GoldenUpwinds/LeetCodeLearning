from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
        return s

Solve = Solution()
s = ["h","e","l","l","o"]
print(Solve.reverseString(s))