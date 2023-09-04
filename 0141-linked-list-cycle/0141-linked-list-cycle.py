# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ptr = head
        visited = set()
        
        while ptr:
            if ptr in visited:
                return True
            ptr2 = ptr
            visited.add(ptr2)
            ptr = ptr.next
            
            
        return False