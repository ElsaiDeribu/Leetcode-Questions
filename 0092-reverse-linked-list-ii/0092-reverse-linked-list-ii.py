# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head.next:
            return head
        
        count = 0
        start = ListNode()
        start.next = head
        end = head
        head = start
        
        while count != left - 1:
            start = start.next
            count += 1
        
        count = 1
        while count != right + 1:
            if count == right:
                temp = end
                end = end.next
                temp.next = None
                
            else:
                end = end.next
                
            count += 1
            
            
        startToRev = start.next
        revStart, revEnd  = self.reverse(startToRev)
        start.next = revStart
        revEnd.next = end
        
        return head.next
            
    def reverse(self, head):
        
        curr = head
        nxt = head.next
        prev = None
        
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt:
                nxt = nxt.next
            
        return (prev, head)
            
        
        
        
        
        
        
        
        
        
        
        
            
            
            