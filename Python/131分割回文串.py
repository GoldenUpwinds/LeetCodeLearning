from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        ss = []

        def check(left,right):
            while left <= right:
                if not s[left] == s[right]:
                    return False
                left,right = left+1, right-1
            return True
        
        def trackback(start_index):
            if start_index == len(s):
                output.append(ss[:])
                return
            
            for i in range(start_index,len(s)):
                if check(start_index,i):
                    ss.append(s[start_index:i+1])
                    trackback(i+1)
                    ss.pop()
            return
        
        trackback(0)
        return output

Solve = Solution()
s = "aab"
print(Solve.partition(s))
