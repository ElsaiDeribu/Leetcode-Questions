"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        ans = []
        deq = Deque([root])
        
        def addLayer():
            
            temp = []
            for i in range(len(deq)):
                if deq[i]:
                    temp.append(deq[i].val)
            ans.append(temp) if temp else None
            
        while deq:
            addLayer()
            
            for i in range(len(deq)):
                node = deq.popleft()
                if node:
                    for child in node.children:
                        deq.append(child)
        
        return ans