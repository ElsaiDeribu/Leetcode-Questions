# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newhead = head
        i = head
        j = head
        counter = 0
        counter_2 = 1
        while i:
            counter += 1
            i = i.next
 
        if counter == 1:
            return None
        
        if n == counter:
            newhead = newhead.next
        
        while j: 
            
            if counter_2  == counter - (n - 1) - 1:
                j.next = j.next.next
                break
            j = j.next
            counter_2 += 1
            
        return newhead   
            