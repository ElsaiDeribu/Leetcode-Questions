# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        
        def dfs(node, prev_total):
            if not node:
                return 0

            h_total = prev_total * 10 + node.val

            if not node.left and not node.right:
                return h_total

            return dfs(node.left, h_total)  + dfs(node.right, h_total)
        
        return dfs(root, 0)