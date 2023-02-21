# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr = head
        
        while ptr:
            
            while ptr.next and ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
                
            ptr = ptr.next
            
        return head