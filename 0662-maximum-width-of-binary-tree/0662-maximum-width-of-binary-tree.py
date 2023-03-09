# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        deq = deque([(root, 1)])
        
        maxLen = 1
        
        
        while deq:
            
            maxLen = max(maxLen, deq[-1][1] - deq[0][1] + 1)
            
            for i in range(len(deq)):
                node, index = deq.popleft()
                
                if node.left:
                    deq.append((node.left, 2 * index))
                    
                if node.right:
                    deq.append((node.right, 2 * index + 1))
                    
                    
        return maxLen
        
        

            
            
            
            
            
            
            
            
            
        
        