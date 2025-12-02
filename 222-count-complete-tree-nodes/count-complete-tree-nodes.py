# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left

            return h

        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right

            return h

        
        lh, rh = left_height(root), right_height(root)

        if lh == rh:
            return (1 << lh) - 1 

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
