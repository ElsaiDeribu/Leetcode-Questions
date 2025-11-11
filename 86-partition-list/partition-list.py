# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left = l_p = ListNode()
        right = r_p = ListNode()

        curr = head

        while curr:
            if curr.val < x:
                l_p.next = curr
                l_p = l_p.next

            else:
                r_p.next = curr
                r_p = r_p.next

            curr = curr.next
            
        r_p.next = None
        l_p.next = right.next

        return left.next


        