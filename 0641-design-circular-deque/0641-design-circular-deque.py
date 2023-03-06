class MyCircularDeque:

    def __init__(self, k: int):
        
        self.myDeq = [None] * k
        self.last = 0
        self.front = (self.last + 1) % k

    def insertFront(self, value: int) -> bool:
        
        if self.myDeq[self.front] == None:
            self.myDeq[self.front] = value
            self.front = (self.front + 1) % len(self.myDeq)
            return True
        
        return False
            

    def insertLast(self, value: int) -> bool:
        
         if self.myDeq[self.last] == None:
            self.myDeq[self.last] = value
            self.last = (self.last - 1) % len(self.myDeq)
            return True
        
         return False
        
        

    def deleteFront(self) -> bool:
        
        temp = (self.front - 1) % len(self.myDeq)
        
        if self.myDeq[temp] == None:
            return False
        
        else:
            self.front = temp
            self.myDeq[self.front] = None
            return True
        

    def deleteLast(self) -> bool:
        
        temp = (self.last +  1) % len(self.myDeq)
        
        if self.myDeq[temp] == None:
            return False
        
        else:
            self.last = temp
            self.myDeq[self.last] = None
            return True
        

    def getFront(self) -> int:
                
        temp = (self.front - 1) % len(self.myDeq)
        
        if self.myDeq[temp] == None:
            return -1
        
        
        return self.myDeq[temp]

        
    def getRear(self) -> int:
        
        temp = (self.last + 1) % len(self.myDeq)
        
        if self.myDeq[temp] == None:
            return -1
        
        
        return self.myDeq[temp]
        

    def isEmpty(self) -> bool:
        
        last = (self.last + 1) % len(self.myDeq)
        front = (self.front - 1) % len(self.myDeq)
        
        if self.myDeq[last] == None and self.myDeq[front] == None:
            return True
        
        
        return False
        

    def isFull(self) -> bool:
        
        if self.myDeq[self.front] != None and self.myDeq[self.last] != None:
            return True
        
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()