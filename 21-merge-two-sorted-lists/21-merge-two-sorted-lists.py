# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sortedLinkedList = list1
        l1 = list1
        l2 = list2
        ans =[]
        while l1 and l2:
            if l1.val == l2.val:
                ans.append(l1.val)
                ans.append(l2.val)
                l1 = l1.next
                l2 = l2.next
            if l1 and l2  and l1.val > l2.val:
                ans.append(l2.val)
                if l2.next:
                    l2  = l2.next
                else:
                    l2 = l2.next
                    break
            if l1 and l2 and l1.val < l2.val:
                ans.append(l1.val)
                if l1.next:
                    l1 = l1.next
                else:
                    l1 = l1.next
                    break
                
        while l1:
            ans.append(l1.val)
            l1 = l1.next
        while l2:
            ans.append(l2.val)
            l2 = l2.next
            
        solution = ListNode()
        head = solution
     
        i = 0  
        while i < len(ans):
            solution.next = ListNode()
            solution = solution.next
            solution.val = ans[i]
            i += 1

        head = head.next
                
        return head