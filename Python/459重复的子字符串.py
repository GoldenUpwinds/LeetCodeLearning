class Solution:
    def findNext(self,next,s):
        j = 0
        next[j] = 0
        for i in range(1,len(s)):
            while j>0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        next = [0] * len(s)
        self.findNext(next,s)
        print(next)

        if next[len(s)-1] != 0 and len(s) % (len(s)-(next[len(s)-1])) == 0:
            return True
        return False

Solve = Solution()
s = "abcabc"
print(Solve.repeatedSubstringPattern(s))
