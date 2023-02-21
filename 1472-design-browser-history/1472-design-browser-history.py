class ListNode:
    def __init__ (self, nxt = None, prev = None, val = None):
        
        self.next = nxt
        self.prev = prev
        self.val = val

class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.head = ListNode()
        self.head.next = ListNode(val = homepage) 
        self.curr = self.head.next

    def visit(self, url: str) -> None:
        
        self.curr.next = ListNode(val = url, prev = self.curr)
        self.curr = self.curr.next
        

    def back(self, steps: int) -> str:
        
        for _ in range(steps):
            if not self.curr.prev:
                return self.curr.val
            
            self.curr = self.curr.prev
            
        return self.curr.val
    
    def forward(self, steps: int) -> str:
        
        for _ in range(steps):
            if not self.curr.next:
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)