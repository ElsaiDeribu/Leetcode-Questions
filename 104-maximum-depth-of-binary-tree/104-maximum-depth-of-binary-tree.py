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
        count = 0
        
        def dfs(count, n):
            count += 1
            if n.left and n.right:
                return max(dfs(count, n.left), dfs(count, n.right))
            elif n.left and not n.right:
                return dfs(count, n.left)
            elif not n.left and  n.right:
                return dfs(count, n.right)
            else:
                return count
            
        return dfs(count, root)
        