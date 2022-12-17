# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        deq = Deque([root])
        
        maximum = float("-inf")
        level = 1
        ans = 1
        
        def findLevelSum():
            total = 0
            for i in range(len(deq)):
                if deq[i]:
                    total += deq[i].val
            return total
        
        
        while deq:
            levelSum = findLevelSum()
            if levelSum > maximum:
                ans = level
                maximum = levelSum
                
            for i in range(len(deq)):
                node = deq.popleft()
                if node:
                    deq.append(node.left) if node.left else None
                    deq.append(node.right) if node.right else None
            level += 1    
            
            
        return ans