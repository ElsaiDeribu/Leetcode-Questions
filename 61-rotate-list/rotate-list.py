# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        k %= length
        if k == 0:
            return head

        edge = length - k - 1
        curr = head
        
        while edge:
            edge -= 1
            curr = curr.next

        new_head = curr.next
        curr.next = None

        temp = new_head

        while temp and temp.next:
            temp = temp.next

        temp.next = head


        return new_head

        

        

