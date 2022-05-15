"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        count= 0
        def dfs(count, n):
            count += 1

            ans = 0
            for i in n.children:
                ans = max(ans, dfs(count, i))
           
            return count if not n.children else ans
         
        return dfs(count, root)