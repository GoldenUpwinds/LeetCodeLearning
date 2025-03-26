from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        caculate_operator = ['+','-','*','/']
        for token in tokens:
            if token in caculate_operator:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num2+num1)
                elif token == '-':
                    stack.append(num2-num1)
                elif token == '*':
                    stack.append(num2*num1)
                elif token == '/':
                    stack.append(int(num2/num1))
            else:
                stack.append(int(token)-int('0'))
        return stack[0]
    
Solve = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solve.evalRPN(tokens))