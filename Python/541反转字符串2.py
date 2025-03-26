class Solution:
    def strPartReverse(self,s,i,j):
        s = list(s)
        while i<j:
            s[i],s[j]=s[j],s[i]
            i,j = i+1,j-1
        return "".join(s)

    def reverseStr(self, s: str, k: int) -> str:
        len_s = len(s)
        for i in range(0,len(s),2*k):
            if i+k <= len_s:
                s = self.strPartReverse(s,i,i+k-1)
                continue
            s = self.strPartReverse(s,i,len_s-1)
        return s
    
Solve = Solution()
s = "abcdefg"
k = 2
print(Solve.reverseStr(s,k))
            