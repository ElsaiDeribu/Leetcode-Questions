"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 1
        self.maxdepth = 0
        
        if not root:
            return 0
        
        def dfs(node, d):
            if node.children:
                d += 1
                for child in node.children:
                    dfs(child, d)
            else:
                self.maxdepth = max(d, self.maxdepth)
                
        dfs(root, depth)
        
        return self.maxdepth