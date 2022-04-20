class MyCircularDeque(object):

    def __init__(self, k):
        
        self.k = k
        self.deque = []
        
    def insertFront(self, value):
        if len(self.deque) < self.k:
            self.deque.insert(0,value)
            return True
        
        return False
        
    def insertLast(self, value):
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        
        return False
        
    def deleteFront(self):
        if self.deque:
            self.deque.pop(0)
            return True
        
        return False
        
    def deleteLast(self):
        if self.deque:
            self.deque.pop()
            return True
        
        return False        

    def getFront(self):
        if self.deque:
            return self.deque[0]
    
        return -1

    def getRear(self):
        
        return self.deque[-1] if self.deque  else -1
    
        
    def isEmpty(self):
        
        return False if self.deque  else True
       
    def isFull(self): 
        
        return True if (len(self.deque) == self.k) else False
        


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