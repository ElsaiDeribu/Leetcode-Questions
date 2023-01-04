# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        self.count = 0
        
        def findGoodPairs(node):
            
            if not node:
                return []
        
        
            if not node.right and not node.left: 
                return [1]
            
            leftDistanceList = findGoodPairs(node.left)
            rightDistanceList = findGoodPairs(node.right)
             
            if leftDistanceList and rightDistanceList:
                for leftItem in leftDistanceList:
                    for rightItem in rightDistanceList:
                        if leftItem + rightItem <= distance:
                            self.count += 1
                            
                            
            for i in range(len(leftDistanceList)):
                leftDistanceList[i] += 1
                
            for j in range(len(rightDistanceList)):
                rightDistanceList[j] += 1
                        
            return leftDistanceList + rightDistanceList         
        
        findGoodPairs(root)
        
        return self.count