class MyQueue:

    def __init__(self):
        self.qu = []

    def push(self, x: int) -> None:
        self.qu.append(x)

    def pop(self) -> int:
        if len(self.qu) == 0:
            return None
        ans = self.qu[0]
        self.qu.pop(0)
        return ans

    def peek(self) -> int:
        if len(self.qu) == 0:
            return None
        return self.qu[0]

    def empty(self) -> bool:
        if len(self.qu) == 0:
             return True
        return False

        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()