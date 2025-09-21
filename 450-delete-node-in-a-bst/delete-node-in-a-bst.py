# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                root = root.right

            elif not root.right:
                root = root.left

            else:
                curr = root.right

                while curr.left:
                    curr = curr.left

                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)


        return root


        

        