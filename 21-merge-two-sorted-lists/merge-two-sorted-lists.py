# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        ans = head


        while list1 or list2:

            if list1 and not list2:
                head.next = list1
                list1 = None

            elif list2 and not list1:
                head.next = list2
                list2 = None

            elif list1.val < list2.val:
                head.next = list1
                list1 = list1.next
                head.next.next = None

            else:
                head.next = list2
                list2 = list2.next
                head.next.next = None


            head = head.next


        return ans.next


