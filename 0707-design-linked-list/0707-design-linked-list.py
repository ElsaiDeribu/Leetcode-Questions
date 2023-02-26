class MyLinkedList:

    def __init__(self):
        
        self.head = ListNode()

    def get(self, index: int) -> int:
        
        currIndex = 0
        curr = self.head.next
        
        while curr and currIndex != index:
            currIndex += 1
            curr = curr.next
        
        if curr :
            return curr.val
            
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        
        newNode = ListNode(val)
        
        newNode.next = self.head.next
        self.head.next = newNode
        

    def addAtTail(self, val: int) -> None:
        
        newNode = ListNode(val)
        prev = self.head
        curr = self.head.next
        
        while curr:
            curr = curr.next
            prev = prev.next
            
        prev.next = newNode
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        currIndex = 0
        newNode = ListNode(val)
        prev = self.head
        curr = self.head.next
        
        while curr and currIndex != index:
            currIndex += 1
            prev = prev.next
            curr = curr.next
        
        if currIndex == index:
            newNode.next = prev.next
            prev.next = newNode 
        

    def deleteAtIndex(self, index: int) -> None:
        
        currIndex = 0
        prev = self.head
        curr = self.head.next
        
        while curr and currIndex != index:
            currIndex += 1
            prev = prev.next
            curr = curr.next
        
        if curr:
            prev.next = prev.next.next
    
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)