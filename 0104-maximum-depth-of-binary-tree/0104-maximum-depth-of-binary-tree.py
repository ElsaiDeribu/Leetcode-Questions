# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(depth, node):
            if not node:
                return depth
            
            depth += 1
            
            leftDepth = dfs(depth, node.left)
            rightDepth = dfs(depth, node.right)
            
            return max(leftDepth, rightDepth)
        
        
        return dfs(0, root)
                