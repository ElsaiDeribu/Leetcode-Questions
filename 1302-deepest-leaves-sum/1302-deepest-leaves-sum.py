# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        deq = deque([root])
        deepestLevel = []
        
        def getLatestLevel():
            temp = []
            for i in range(len(deq)):
                temp.append(deq[i].val)
                
            return temp            

        
        while deq:
            
            deepestLevel = getLatestLevel()
            
            for _ in range(len(deq)):
                
                currNode = deq.popleft()
                
                deq.append(currNode.left) if currNode.left else None
                deq.append(currNode.right) if currNode.right else None
            
        
        return sum(deepestLevel)