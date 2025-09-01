# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        layer = deque([root])
        level = 1
        largest = [1, root.val]


        while layer:
                
            total = 0
            level += 1

            for _ in range(len(layer)):
                node = layer.popleft()

                if node.left:
                    total += node.left.val
                    layer.append(node.left)

                if node.right:
                    total += node.right.val
                    layer.append(node.right)

            if layer:
                if total > largest[1]:
                    largest[1] = total
                    largest[0] = level


        return largest[0]


            


        