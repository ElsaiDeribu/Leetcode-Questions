# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = head 
        i = head
        j = head.next
        
        while i.next: 
            while j:
                if j.val < i.val:
                    i.val, j.val = j.val, i.val
                    
                j = j.next
                    
            i = i.next
            j = i.next
            
        return newhead
            