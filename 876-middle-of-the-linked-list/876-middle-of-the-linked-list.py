# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        j = head
        
        while True:
            if j.next == None:
                return i
            
            if j.next.next == None:
                return i.next
             
            i = i.next
            j = j.next.next
        