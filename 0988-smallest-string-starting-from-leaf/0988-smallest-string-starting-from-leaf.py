# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        
        self.smallest = None
        
        def findSmallest(node, string):
            if not node:
                return
            
            string += chr(node.val + 97)
            
            if not node.left and not node.right:
                reversedString = string[:: -1]
                
                if not self.smallest or self.smallest > reversedString:
                    self.smallest = reversedString

                    
            findSmallest (node.left, string)
            findSmallest(node.right, string)
            
        
        findSmallest(root, "")
        
        return self.smallest
            
            
            
            
        
            
        
        
 



