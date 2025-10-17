# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        ans = []
        deq = deque([root] if root else [])

        while deq:

            layer = []

            for _ in range(len(deq)):
                node = deq.popleft()
                layer.append(node.val) 

                if node.left: deq.append(node.left)
                if node.right: deq.append(node.right)


            ans.append(layer[:])





        return ans
