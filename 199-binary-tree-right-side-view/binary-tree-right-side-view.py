# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        deq = deque()
        ans = []

        if root:
            deq.append(root)
            ans.append(root.val)
            

        while deq:

            for _ in range(len(deq)):
                node = deq.popleft()

                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)

            if deq:
                ans.append(deq[-1].val)


        return ans
        