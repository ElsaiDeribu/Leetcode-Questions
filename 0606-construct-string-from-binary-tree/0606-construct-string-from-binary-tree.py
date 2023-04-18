# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        ans = []
        
        def preOrder(node):
            
            if not node:
                return
            
            
            ans.append("(")
            ans.append(str(node.val))
            
            if (not node.left) and (node.right):
                ans.append("()")
                
            preOrder(node.left)
            preOrder(node.right)
            ans.append(")")
            
        
        preOrder(root)
        
        return ''.join(ans[1:-1])
        
        
        