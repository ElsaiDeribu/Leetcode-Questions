# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def dfs(s, dir, node):

            self.ans = max(self.ans, s)

            if not node:
                return 
            

            if dir == "left":
                dfs(0, "left", node.left)
                dfs(s + 1, "right", node.right)

            else:
                dfs(s + 1, "left", node.left)
                dfs(0, "right", node.right )


        dfs(0, "left", root.left)
        dfs(0, "right", root.right)


        return self.ans
    