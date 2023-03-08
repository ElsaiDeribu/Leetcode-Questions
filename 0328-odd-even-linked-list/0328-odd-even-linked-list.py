# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head:
            return 
        
        curr = head
        prev = head.next
        
        while prev and prev.next:
            temp = prev.next
            prev.next = prev.next.next
            temp.next = curr.next
            curr.next = temp
            curr = curr.next
            prev = prev.next
            
        return head
            
        

                
                
                
        