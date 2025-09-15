# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        left = ListNode()
        left.next = head
        right = head
        head = left
        count = 1
        
        while right and count != n + 1:
            count += 1
            right = right.next
            
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next
            
        
        return head.next
            
            