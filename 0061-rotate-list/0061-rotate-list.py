# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        if not head:
            return head
        
        length = 0
        curr = head
        
        # get linkedList length
        while curr:
            length += 1
            curr = curr.next
         
        netRotation = k % length
        
        if netRotation == 0:
            return head
        
        prev = length - netRotation 
        count = 1
        curr = head
        
        while count != prev:
            curr = curr.next
            count += 1
            
        temp = curr
        
        while curr.next:
            curr = curr.next
                
        curr.next = head
        head = temp.next
        temp.next = None
        
        return head
        
        
        
        