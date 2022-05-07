# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev, current = head, head.next
        flag = 0
      
        while current and prev.val == current.val:
            while current and prev.val == current.val:
                current = current.next
                
            head = current
            prev = head
            if current:
                current = prev.next
            
        while current:
            flag = 0
            while current.next and current.val == current.next.val :
                current = current.next
                flag = 1
            if flag  == 1:
                prev.next = current.next
                current = prev.next
                continue
            prev = prev.next
            current = prev.next
            
        return head