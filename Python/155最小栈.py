class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if self.minstack[-1] == val:
            self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

import sys
import ast

def main():
    data = sys.stdin.read().strip().splitlines()
    actions = ast.literal_eval(data[0])
    nums = ast.literal_eval(data[1])

    testStack = None

    for i in range(len(actions)):
        action = actions[i]
        if action == "MinStack":
            testStack = MinStack()
        elif action == "push":
            testStack.push(nums[i])
        elif action == "getMin":
            print(testStack.getMin())
        elif action == "top":
            print(testStack.top())
        elif action == "pop":
            testStack.pop()
    
    return

if __name__ == "__main__":
    main()