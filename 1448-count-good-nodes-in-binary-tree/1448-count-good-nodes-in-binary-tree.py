# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 1
        
        def countGoodNodes(node, nodesTillNow):
            
            if not node:
                return 
            
            if nodesTillNow:
                largestTillNow = -nodesTillNow[0]
                if node.val >= largestTillNow:
                    self.count += 1
                
                
            heappush(nodesTillNow, -node.val)
            
            countGoodNodes(node.left, nodesTillNow)
            countGoodNodes(node.right, nodesTillNow)
            
            currNodeIndex = nodesTillNow.index(-node.val)
            nodesTillNow.pop(currNodeIndex)
            heapify(nodesTillNow)
            
            
            
        countGoodNodes(root, [])
        
        return self.count