# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        if not root:
            return 0
        
        def dfs(node):
            if node.left or node.right:
                l = dfs(node.left) if node.left else 0
                r = dfs(node.right) if node.right else 0
                self.total += abs(l - r)
                
                return l + r + node.val
                
            else:
                return node.val
            
        dfs(root)
        
        return self.total