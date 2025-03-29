from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        output = []

        def isValid(s):
            if not s:
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            if not 0 <= int(s) <= 255:
                return False
            return True

        def trackback(start_index):
            if start_index == len(s) and len(path) == 4 and isValid(path[-1]):
                output.append(".".join(path))
                return
            
            if len(path) == 4 or start_index == len(s):
                return
            
            if s[start_index] == '0':
                path.append('0')
                trackback(start_index+1)
                path.pop()
                return

            for i in range(start_index,len(s)):
                if isValid(s[start_index:i+1]):
                    path.append(s[start_index:i+1])
                    trackback(i+1)
                    path.pop()
                else:
                    continue
            return

        trackback(0)
        return output

Solve = Solution()
s = "25525511135"
print(Solve.restoreIpAddresses(s))
            
