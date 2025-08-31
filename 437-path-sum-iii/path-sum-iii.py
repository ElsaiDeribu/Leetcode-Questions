# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        
        def dfs(pref, total, node):

            if not node:
                return 0

            total += node.val
            count = pref[total - targetSum]

            pref[total] += 1
            
            res_l = dfs(pref, total , node.left)
            res_r = dfs(pref, total , node.right)

            pref[total] -= 1


            return res_l + res_r + count

        pref = defaultdict(int)
        pref[0] = 1



        return dfs(pref, 0, root)



