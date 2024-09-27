class MyStack:

    def __init__(self):
        self.stk = deque()

    def push(self, x: int) -> None:
        self.stk.append(x)

    def pop(self) -> int:
        for i in range(len(self.stk)-1):
            self.push(self.stk.popleft())
        return self.stk.popleft()

    def top(self) -> int:
        return self.stk[-1]
        
    def empty(self) -> bool:
        return len(self.stk) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()