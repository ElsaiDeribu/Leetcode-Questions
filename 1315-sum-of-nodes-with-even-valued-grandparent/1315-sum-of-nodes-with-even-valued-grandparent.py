# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        
        self.count = 0
        
        def countNodes(node, nodesTillNow):
            
            if not node:
                return
            
            if len(nodesTillNow) >= 2:
                if nodesTillNow[-2] % 2 == 0:
                    self.count += node.val
                    
            nodesTillNow.append(node.val)
            
            countNodes(node.left, nodesTillNow)
            countNodes(node.right, nodesTillNow)
            
            nodesTillNow.pop()
            
        countNodes(root, [])  
            
        return self.count
            