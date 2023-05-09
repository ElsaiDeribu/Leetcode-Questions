# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        
        for lst in lists:
            head = lst
            while head:
                heappush(heap, head.val)
                head = head.next
                
       
        ans = ListNode()
        head = ans
        while heap:
            head.next = ListNode(heappop(heap))
            head = head.next
            
        return ans.next