# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        deq = Deque([root])
        currLevel = 0
        
        def valid():
            if currLevel % 2 == 0:
                prev = deq[0].val
                if prev % 2 == 0:
                    return False
                
                for i in range(1, len(deq)):
                    if (deq[i].val % 2 == 0) or (prev >= deq[i].val):
                        return False
                    prev = deq[i].val
              
            else:
                prev = deq[0].val
                if prev % 2:
                    return False
                 
                for i in range(1, len(deq)):
                    if deq[i].val % 2 or prev <= deq[i].val:
                        return False
                    prev = deq[i].val
            return True
               
        while deq:
            
            if not valid():
                return False
                
            for i in range(len(deq)):
                node = deq.popleft()
                
                deq.append(node.left) if node.left else None
                deq.append(node.right) if node.right else None
            currLevel += 1
            
        return True