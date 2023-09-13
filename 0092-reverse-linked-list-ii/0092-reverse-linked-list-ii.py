# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
        def reverse(start, size):
            
            tail = start
            prev = None
            curr = start
            nxt = start.next 
            
            while size :
                
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next if nxt else None
                
                size -= 1
              
            tail.next = curr
            return prev
        
        
        temp = ListNode()
        temp.next = head
        head = temp
        
        for _ in range(left - 1):
            temp = temp.next
                    

        prev = reverse(temp.next, right - left + 1)
        temp.next = prev
        return head.next
        
        
                
                
                
                
            
        
                
                
            
            