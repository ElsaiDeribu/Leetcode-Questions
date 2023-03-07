# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def check(node1, node2):
            
            if not node1 and not node2:
                return True
            
            elif (not node1 and node2) or (not node2 and node1):
                return False
                
            elif node1.val != node2.val:
                return False
            
            
            return check(node1.left, node2.left) and check(node1.right, node2.right)
                
                
        return check(p, q)
            
            
            
            
            
            
            
            
        