# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        listOfNodes = []
        i, j, ans = head, head, head
        while i :
            listOfNodes.append(i.val)
            i = i.next
        
        listOfNodes.sort()
        
        for i in listOfNodes:
            j.val = i
            j = j.next
            
        return ans
        
            
#         prev, j, i = None, head, head
        
#         while i:
#             while j.next:
                
#                 if j.next.val < i.val:
#                     temp = j.next
#                     # print(temp)
#                     j.next = j.next.next
#                     temp.next = i
#                     if prev:
#                         prev.next = temp
#                     i = temp
#                     if not prev:
#                         head = i
#                     j = i
                    
                     
#                 j = j.next
#             prev = i
#             i = i.next
#             j = i
            
#         return head
                    
            