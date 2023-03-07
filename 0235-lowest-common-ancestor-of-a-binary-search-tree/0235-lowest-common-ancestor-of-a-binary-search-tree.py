# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        def postOrder(node):
            
            if not node:
                return 
            
            if node == q or node == p:
                return node
            
            left = postOrder(node.left)
            right = postOrder(node.right)
            
            if (left == q and right == p) or ((right == q and left == p) ) :
                return node
            
            if left and not right:
                return left
            
            elif right and not left:
                return right
            
            return
          
        
        return postOrder(root)
            
            
            
            