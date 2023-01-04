# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        self.pathValues = []
        
        
        def findPath(node, nodesTillNow, SumTillNow): 
            if not node:
                return 
            
            nodesTillNow.append(node.val)
            SumTillNow += node.val
            
            if not node.right and not node.left:
                
                if SumTillNow == targetSum:
                    self.pathValues.append(nodesTillNow[:])
                    
                    
            findPath(node.left, nodesTillNow, SumTillNow)
            findPath(node.right, nodesTillNow, SumTillNow)
            
            nodesTillNow.pop()
            
            
        findPath(root, [], 0)
        
        return self.pathValues
                
        