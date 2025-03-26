class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        self.instack.append(x)
        

    def pop(self) -> int:
        if self.outstack:
            return self.outstack.pop()
        while self.instack:
            self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        

    def peek(self) -> int:
        peek_output = self.pop()
        self.outstack.append(peek_output)
        return peek_output
        

    def empty(self) -> bool:
        if not self.instack and not self.outstack:
            return True
        return False

def TestFunction(Actions, Nums):
    output = []
    Queue = None
    for Index in range(len(Actions)):
        if Actions[Index] == "MyQueue":
            output.append(None)
            Queue = MyQueue()
        elif Actions[Index] == "push":
            output.append(None)
            Queue.push(Nums[Index][0])
        elif Actions[Index] == "pop":
            output.append(Queue.pop())
        elif Actions[Index] == "peek":
            output.append(Queue.peek())
        elif Actions[Index] == "empty":
            output.append(Queue.empty())
    return output

Actions = ["MyQueue", "push", "push", "peek", "pop", "empty"]
Nums = [[], [1], [2], [], [], []]
print(TestFunction(Actions,Nums))
