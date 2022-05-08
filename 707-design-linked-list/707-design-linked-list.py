class MyLinkedList:
    
    class ListNode:
        def __init__(self, val = 0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = ListNode()
        self.insertedAtHead = 0 
        

    def get(self, index: int) -> int:
        self.head_1 = self.head
        self.counter = 0
        
        if self.insertedAtHead == 0:
            return -1
        
        if index < 0:
            return -1
        
        while self.head_1:
            if self.counter == index:
                return self.head_1.val
            self.head_1 = self.head_1.next
            self.counter += 1
        return -1
            

    def addAtHead(self, val: int) -> None:
        
            
        if self.head.val == 0 and self.insertedAtHead == 0  :
            self.head.val = val
            self.insertedAtHead = 1
        else:
            self.nodeToInsert = ListNode(val)
            self.nodeToInsert.next  = self.head
            self.head = self.nodeToInsert
            
        
    def addAtTail(self, val: int) -> None:
        
        if self.head.val == 0 and self.insertedAtHead == 0  :
            self.head.val = val
            self.insertedAtHead = 1
            return
        
        self.head_1 = self.head
        nodeToInsert = ListNode(val)
        
        while self.head_1.next:
            self.head_1 = self.head_1.next
        
        self.head_1.next = nodeToInsert
        

    def addAtIndex(self, index: int, val: int) -> None:
        self.head_1 = self.head
        self.nodeToInsert = ListNode(val)
        self.counter = 0 
        
        if index == 0 and self.head.val == 0 and self.insertedAtHead == 0  :
            self.head.val = val
            self.insertedAtHead = 1
            return

        if index == 0 :
            self.nodeToInsert.next = self.head_1
            self.head = self.nodeToInsert
        
        if self.insertedAtHead == 0:
            return
        
        while self.head_1.next:
            if self.counter + 1 == index:
                self.nodeToInsert.next = self.head_1.next
                self.head_1.next = self.nodeToInsert
                break
                
            self.head_1 = self.head_1.next
            self.counter += 1
        if self.counter + 1 == index:
            self.head_1.next = self.nodeToInsert

    def deleteAtIndex(self, index: int) -> None:
        self.head_1 = self.head
        self.counter = 0

        if index == 0 :
            self.head = self.head.next
        
        while self.head_1.next:
            if self.counter + 1 == index:
                self.head_1.next = self.head_1.next.next
                break  
             
            self.head_1 = self.head_1.next
            self.counter += 1
            
    
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)