# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        dic = defaultdict(int)
        mode = []
        
        def preOrder(node):
            if not node:
                return
            
            dic[node.val] += 1
            
            preOrder(node.left)
            preOrder(node.right)
            
        preOrder(root)
        
        dic = sorted(dic.items(), key = lambda x: x[1], reverse = True, )
        
        i = 0
        while i < len(dic) and dic[i][1] == dic[0][1]:
            mode.append(dic[i][0])
            i += 1
            
        return mode