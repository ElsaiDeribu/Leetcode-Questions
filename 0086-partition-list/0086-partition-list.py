# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        if not head:
            return 
        
        temp = ListNode()
        temp.next = head
        head = temp
        
        position = head
            
        while position.next and position.next.val < x:
            position = position.next
            
            
        curr = position
        
        
        while curr and curr.next: 
            if curr.next.val < x:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = position.next
                position.next = temp
                position = position.next
                
            else:   
                curr = curr.next
            
        return head.next
            
        
            
            