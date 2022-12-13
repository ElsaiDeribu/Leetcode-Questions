# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        deq = Deque([root])
        
        def findAv():
            n = len(deq)
            total = 0
            for i in range(len(deq)):
                if deq[i]:
                    total += deq[i].val
                else:
                    n -= 1
            return total / n if n else 0 
        
        
        while deq:
            ans.append(findAv())
            for i in range(len(deq)):
                temp = deq.popleft()
                if temp:
                    deq.append(temp.left)
                    deq.append(temp.right)
                
        ans.pop()    
        return ans
        
        