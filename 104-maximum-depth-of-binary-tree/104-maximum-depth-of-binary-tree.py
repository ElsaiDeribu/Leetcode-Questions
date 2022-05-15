# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(count, n):
            count += 1
            if n.left or n.right:
                return  max(dfs(count, n.left) if n.left else 0, dfs(count, n.right) if n.right else 0)
            else:
                return count
            
        return dfs(0, root)
        