# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        firstFlip = 1
        
        while current and current.next:
            nxt = current.next
            if firstFlip:
                head = nxt
                firstFlip = 0
            current.next = nxt.next
            nxt.next = current
            if prev:
                prev.next = nxt
            prev  = current
            current = current.next
        
        return head
        