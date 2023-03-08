# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
            
        def build(node1, node2):
            if not node1 and not node2:
                return 
            
            if node1 and not node2:
                return node1
            
            elif not node1 and node2:
                return node2
                
            else:
                node1.val = node1.val + node2.val
                
                node1.left = build(node1.left, node2.left)
                node1.right = build(node1.right, node2.right)
            
                return node1
            
        
        return build(root1, root2)

        
    