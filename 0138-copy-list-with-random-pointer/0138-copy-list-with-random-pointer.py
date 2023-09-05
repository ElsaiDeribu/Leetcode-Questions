"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        mapping = defaultdict()
        curr = head
        
        while curr:
            mapping[curr] = ListNode(curr.val)
            curr = curr.next
            
        curr = head
        
        while curr:
            mapping[curr].next = mapping[curr.next] if curr.next else None
            mapping[curr].random = mapping[curr.random] if curr.random else None
            curr = curr.next
            
        return mapping[head] if head else None
            
            
        
            
        