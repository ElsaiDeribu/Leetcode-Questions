# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        deq = Deque([root])
        count = 1       
        while  deq:
            for i in range(len(deq)):
                node = deq.popleft()
                if node:
                    if node.left:
                        count += 1
                        deq.append(node.left)
                    if node.right:
                        count += 1
                        deq.append(node.right)

        return count if root else 0