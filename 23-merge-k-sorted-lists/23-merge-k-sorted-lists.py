# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        ans = []
        ansList = ListNode()
      
        for i in lists:
            while i:
                heappush(heap, i.val)
                i = i.next
                
        for i in range(len(heap)):
            a = heappop(heap)
            ans.append(a)
            
        if not ans:
            return
            
        ansList.val = ans[0]
        head = ansList
        
        for i in range(1,len(ans)):
            ansList.next = ListNode(ans[i])
            ansList = ansList.next
            
            
        return head