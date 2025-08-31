# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.ans = 0

        def dfs(node, mx):
            if not node:
                return


            if node.val >= mx:
                self.ans += 1

            dfs(node.left, max(mx, node.val))
            dfs(node.right, max(mx, node.val))

        dfs(root, float("-inf"))

        return self.ans
