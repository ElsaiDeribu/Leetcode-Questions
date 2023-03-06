class MyCircularQueue:

    def __init__(self, k: int):
        
        self.queue = [None] * k
        
        self.last = 0
        self.front = (self.last + 1) % k
        

    def enQueue(self, value: int) -> bool:
        
        if self.queue[self.last] == None:
            self.queue[self.last] = value
            self.last = (self.last - 1) % len(self.queue)
            return True
        
        return False
         
        
        
    def deQueue(self) -> bool:
        
        front = (self.front - 1) % len(self.queue)
        
        if self.queue[front] != None:
            self.front = front
            self.queue[front] = None
            return True
        
        return False
        

    def Front(self) -> int:
        
        front = (self.front - 1) % len(self.queue)
        
        if self.queue[front] != None:
            return self.queue[front] 

        return -1
        

    def Rear(self) -> int:
        
        last = (self.last + 1) % len(self.queue)

        if self.queue[last] != None:
            return self.queue[last] 

        return -1            

    def isEmpty(self) -> bool:
        
        last = (self.last + 1) % len(self.queue)

        if self.queue[last] == None:
            return True

        return False
        

    def isFull(self) -> bool:
        
        if self.queue[self.last] != None:
            return True

        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()