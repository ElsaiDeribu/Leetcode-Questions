class MinStack:
    
    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        

    def pop(self) -> None:
        if len(self.st) == 0:
            return None
        self.st.pop()

    def top(self) -> int:
        if len(self.st) == 0:
            return None
        return self.st[-1]

    def getMin(self) -> int:
        min = self.st[0]
        if len(self.st) == 0:
            return None
        for i in self.st:
            if i < min:
                min = i
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()