import collections

class MyStack:

    def __init__(self):
        self.main_deque = collections.deque()
        self.sub_deque = collections.deque()

    def push(self, x: int) -> None:
        self.main_deque.appendleft(x)
        

    def pop(self) -> int:
        len_deque = len(self.main_deque)
        while len_deque > 1:
            self.sub_deque.appendleft(self.main_deque.pop())
            len_deque -= 1
        output = self.main_deque.pop()
        self.main_deque = self.sub_deque
        self.sub_deque = collections.deque()
        return output

    def top(self) -> int:
        output = self.pop()
        self.main_deque.appendleft(output)
        return output

    def empty(self) -> bool:
        if not self.main_deque:
            return True
        return False


def TestFunction(Actions, Nums):
    output = []
    Queue = None
    for Index in range(len(Actions)):
        if Actions[Index] == "MyStack":
            output.append(None)
            Queue = MyStack()
        elif Actions[Index] == "push":
            output.append(None)
            Queue.push(Nums[Index][0])
        elif Actions[Index] == "pop":
            output.append(Queue.pop())
        elif Actions[Index] == "top":
            output.append(Queue.top())
        elif Actions[Index] == "empty":
            output.append(Queue.empty())
    return output

Actions = ["MyStack", "push", "push", "top", "pop", "empty"]
Nums = [[], [1], [2], [], [], []]
print(TestFunction(Actions,Nums))