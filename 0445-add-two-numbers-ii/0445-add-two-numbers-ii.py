# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        lst = ''
        lst2 = ''
        
        ls = l1
        while ls :
            lst += str(ls.val)
            ls = ls.next
            
        ls = l2
        while ls :
            lst2 += str(ls.val)
            ls = ls.next
            
        lst = str(int(lst) + int(lst2))
        
        head = ListNode()
        itr = head

        
        for i in range(len(lst)):

                itr.val = int(lst[i])
                if i != len(lst) - 1:
                    itr.next = ListNode()
                    itr = itr.next
                

        return head
                
        
        

            
        