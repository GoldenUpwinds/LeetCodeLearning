class Solution:
    def cutSpace(self,s):
        s = list(s)
        startIndex = 0
        while s[startIndex] == ' ':
            startIndex += 1
        slowPointer = 0
        for fastPointer in range(startIndex,len(s)):
            if fastPointer > 0 and s[fastPointer] == ' ' and s[fastPointer] == s[fastPointer-1]:
                continue
            else:
                s[slowPointer] = s[fastPointer]
                slowPointer += 1
        if slowPointer > 0 and s[slowPointer-1] == ' ':
            return s[:slowPointer-1]
        else:
            return s[:slowPointer]

    def reverseWords(self, s: str) -> str:
        s = self.cutSpace(s)
        s[:] = reversed(s)
        wordFlag = False
        start, end = 0, 0
        for index in range(len(s)):
            if not wordFlag and s[index] != ' ':
                wordFlag = True
                start = index
            elif wordFlag and s[index] == ' ':
                end = index
                wordFlag = False
                s[start:end] = reversed(s[start:end])
            elif wordFlag and index == len(s) - 1:
                s[start:] = reversed(s[start:])
        return "".join(s)

Solve = Solution()
s = "  hello world  "
print(Solve.reverseWords(s))