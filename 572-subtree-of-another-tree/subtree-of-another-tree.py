# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        
        def check(node1, node2):

            if (node1 and not node2) or (node2 and not node1): return False

            if not node1 and not node2: return True

            if node1.val != node2.val: return False

            left = check(node1.left, node2.left)
            # pruning (makes no difference for asymptotic time complexity)
            if left == False: return False

            right = check(node1.right, node2.right)
  
            return  right




        def dfs(node1, node2):
            if not node1: return False
  
            if check(node1, node2) == True: return True

            left = dfs(node1.left, node2)
            if left == True: return True

            right = dfs(node1.right, node2)

            return right


        return dfs(root, subRoot)
        

        