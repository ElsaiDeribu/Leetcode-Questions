# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        deq = Deque([root])
        def ispal():
            for i in range(len(deq) // 2):
                if not deq[i] and deq[-i - 1]:
                    return False
                
                if deq[i] and not deq[-i - 1]:
                    return False
                    
                if (deq[i] and deq[-i - 1]) and deq[i].val != deq[-i - 1].val:
                    return False
            return True
        
        while deq:
            if not ispal():
                return False
                
            for j in range(len(deq)):
                m = deq.popleft()
                if m:
                    deq.append(m.left)
                    deq.append(m.right)   
                
                        
        return True