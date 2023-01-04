# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        self.totalSum = 0
        
        def findSum (node, string):
            if not node:
                return
            
            string += str(node.val)
            
            if not node.right and not node.left:
                self.totalSum += int(string)
                
            findSum(node.left, string)
            findSum(node.right, string)
                
                
        findSum(root, "")
        
        
        return self.totalSum
        
        
                
            
            
        