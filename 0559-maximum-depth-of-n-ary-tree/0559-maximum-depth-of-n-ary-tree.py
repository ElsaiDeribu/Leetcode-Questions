"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        
        def dfs(node, depth):
            if not node:
                return depth
            
            depth += 1
            mxdepth = depth
            
            for child in node.children:
                mxdepth = max(dfs(child, depth), mxdepth)
                
            return mxdepth
                
        
        return dfs(root, 0)