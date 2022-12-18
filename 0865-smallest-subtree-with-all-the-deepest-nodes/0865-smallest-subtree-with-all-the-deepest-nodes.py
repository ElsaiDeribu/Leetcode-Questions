# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        
        def getDeepest(node):
            
            if not node:
                return (0, None)
            
            leftDepth = getDeepest(node.left)
            rightDepth = getDeepest(node.right)
        
        
            if leftDepth[0] == rightDepth[0]:
                return (leftDepth[0] + 1, node)
            elif leftDepth[0] > rightDepth[0]:
                return (leftDepth[0] + 1, leftDepth[1])
            else:
                return (rightDepth[0] + 1, rightDepth[1] )
            
        return getDeepest(root)[1]