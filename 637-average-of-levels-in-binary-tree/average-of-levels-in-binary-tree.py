# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        ans = []
        deq = deque([root])

        while deq:
            total = 0
            count = len(deq)

            for _ in range(len(deq)):
                node = deq.popleft()
                total += node.val

                if node.left: deq.append(node.left)
                if node.right: deq.append(node.right)

            ans.append(total / count)

        return ans
        