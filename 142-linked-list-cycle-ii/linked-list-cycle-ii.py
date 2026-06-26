# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow, fast = head, head
        loop_exists = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                loop_exists = True
                break

        if not loop_exists:
            return

        pos = 0

        while head != slow:
            slow = slow.next
            head = head.next
            pos += 1

        return slow