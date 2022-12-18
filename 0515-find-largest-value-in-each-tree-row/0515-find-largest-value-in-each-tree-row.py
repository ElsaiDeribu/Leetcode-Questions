# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        deq = Deque([root])
        ans = []
        if not root:
            return []
        
        def findLevelMax():
            levelMax = float("-inf")
            for i in range(len(deq)):
                levelMax = max(levelMax, deq[i].val)
                
            return levelMax
        
        
        while deq:
            ans.append(findLevelMax())
            for i in range(len(deq)):
                node = deq.popleft()
                deq.append(node.left) if node.left else None
                deq.append(node.right) if node.right else None
        
        return ans