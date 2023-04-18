# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        accumulator = []
        ans = 0
        
        def preOrder(node):
            nonlocal accumulator
            nonlocal ans
            
            if not node:
                return
                
            accumulator.append(str(node.val))
                           
            if not node.left and not node.right:
                ans += int(''.join(accumulator))
            

            preOrder(node.left)
            preOrder(node.right)
            
            accumulator.pop()
                           
        preOrder(root)
                           
        return ans
            
            
        