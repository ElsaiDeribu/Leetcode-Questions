class MinStack:

    def __init__(self):
        
        self.stack = []
        self.minStack = []
        self.currMin = float("inf")
        

    def push(self, val: int) -> None:
        
        self.currMin = min(self.currMin, val)
        self.stack.append(val)
        self.minStack.append(self.currMin)
        

    def pop(self) -> None:
        
        self.stack.pop()
        self.minStack.pop()
        self.currMin = self.minStack[-1] if self.minStack else float("inf")
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()