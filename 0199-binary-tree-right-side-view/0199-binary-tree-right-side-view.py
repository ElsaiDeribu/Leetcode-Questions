# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        deq = Deque([root])
        ans = []
        
        
        while deq and root:
            rightSide = deq[-1]
            ans.append(rightSide.val)
            for i in range(len(deq)):
                node = deq.popleft()
                if node:
                    deq.append(node.left) if node.left else None
                    deq.append(node.right) if node.right else None
                    
        return ans
        