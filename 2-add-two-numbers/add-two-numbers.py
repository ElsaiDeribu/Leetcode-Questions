# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        head1 = l1
        head2 = l2

        num1 = 1

        while head1:

            num1 *= 10
            num1 += head1.val
            head1 = head1.next

        num2 = 1
        while head2:

            num2 *= 10
            num2 += head2.val
            head2 = head2.next

        num1 = int(str(num1)[1:][::-1])
        num2 = int(str(num2)[1:][::-1])

        num3 = str(num1 + num2)
        head = l1
        print(num1, num2, num3)
        for i in range(len(num3) - 1, -1, -1):
            if not head.next and i >  0:
                head.next = ListNode()

            head.val = int(num3[i])
            head = head.next



        return l1



