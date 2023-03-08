# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        
        def postOrder(node):
            
            if not node:
                return [0, 0, 0]
#                [sumOfSubTreeVals, CountOfSubTrees, CountOfAvgEqualToValue]
        
            left = postOrder(node.left)
            right = postOrder(node.right)
            
            total = left[0] + right[0] + node.val
            count = left[1] + right[1] + 1
            countOfValid = left[2] + right[2]
            
            
            if count > 0:
                avg = total // count
                
                if avg == node.val:
                     countOfValid += 1
                    
            return [total, count, countOfValid]
        
        
        return postOrder(root)[2]
        
        
        
                
                
