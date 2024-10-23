class MyQueue:

    def __init__(self):
        self.stk = deque()
        
    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stk) - 1):
            self.stk.appendleft(self.stk.pop())
        return self.stk.pop()

    def peek(self) -> int:
        for i in range(len(self.stk) - 1):
            self.stk.appendleft(self.stk.pop())
        last = self.stk.pop()
        self.stk.appendleft(last)
        return last
        

    def empty(self) -> bool:
        return len(self.stk) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()