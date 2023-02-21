# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast, slow = head, head
        
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                l1 = head
                l2 = fast
                
                while l1 != l2:
                    l1 = l1.next
                    l2 = l2.next
                    
                return l1
                
                
        return None
        