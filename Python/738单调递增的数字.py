class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n = list(str(n))
        flag = len(n)

        for i in range(len(n)-1,0,-1):
            if n[i] < n[i-1]:
                n[i-1] = str(int(n[i-1])-1)
                flag = i
  
        for i in range(flag,len(n)):
            n[i] = '9'

        return int(''.join(n))


Solve = Solution()
n = 1234
print(Solve.monotoneIncreasingDigits(n))
