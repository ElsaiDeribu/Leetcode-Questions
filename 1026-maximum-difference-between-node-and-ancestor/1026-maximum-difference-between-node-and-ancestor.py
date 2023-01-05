# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        self.maxDifference = 0
        
        def findMax(node, minTillNow, maxTillNow):
            
            if not node:
                return 
            
            if minTillNow != None and maxTillNow != None:
                
                candidateMaxDiff = max(abs(node.val - minTillNow), abs(node.val - maxTillNow)) 
                
                self.maxDifference = max(self.maxDifference, candidateMaxDiff)
                
                if node.val > maxTillNow:
                    maxTillNow = node.val
                if node.val < minTillNow:
                    minTillNow = node.val
                    
            else:
                maxTillNow =  node.val
                minTillNow = node.val
                
            findMax(node.left, minTillNow, maxTillNow)
            findMax(node.right, minTillNow, maxTillNow)
                
                
                
            
        findMax(root, None, None)
            
            
        return self.maxDifference

