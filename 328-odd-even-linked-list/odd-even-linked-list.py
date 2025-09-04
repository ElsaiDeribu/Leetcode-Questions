# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        write = head
        read = head.next if head else None

        while read and read.next:
            temp = read.next 
            read.next = read.next.next

            temp.next = write.next
            write.next = temp

            write = write.next
            read = read.next


        return head
            

            

            

                





        