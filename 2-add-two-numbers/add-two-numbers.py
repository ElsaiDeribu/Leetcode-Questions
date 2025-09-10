# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        num1 = []
        num2 = []

        h1, h2 = l1, l2

        while h1:
            num1.append(str(h1.val))
            h1 = h1.next

        while h2:
            num2.append(str(h2.val))
            h2 = h2.next

        num1 = int(''.join(num1[::-1]))
        num2 = int(''.join(num2[::-1]))

        num = str(num1 + num2)[::-1]


        head = l1

        for i, n in enumerate(num):
            head.val = int(n)
            if not head.next and i < len(num) - 1:
                head.next = ListNode()
            head = head.next

        return l1

