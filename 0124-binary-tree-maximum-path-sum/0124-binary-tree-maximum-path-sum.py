# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return 0
            
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            poss1 = left + right + node.val
            poss2 = left + node.val
            poss3 = right + node.val
            poss4 = node.val
            
            ans = max(ans, poss1, poss2, poss3, poss4)
            
            return max(poss2, poss3, poss4)
        
        dfs(root)
        
        return ans
