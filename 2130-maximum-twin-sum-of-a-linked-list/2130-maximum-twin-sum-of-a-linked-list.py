# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast, slow, start = head, head, head
        largestSum = 0
        
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next
        end = fast.next  
        
        prev = slow
        slow = slow.next
        prev.next = None
        while slow :
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
            
        while start:
            largestSum = max(largestSum, start.val + end.val)
            start = start.next
            end = end.next
            
        return largestSum
            
        
            
          
            