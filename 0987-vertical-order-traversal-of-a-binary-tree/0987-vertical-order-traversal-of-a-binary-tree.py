# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dic = defaultdict(list)
        
        
        def recur(node, row, col):
            if not node:
                return
            
            dic[col].append((row, node.val))
            
            recur(node.left, row + 1, col - 1)
            recur(node.right, row + 1, col + 1)
            
        recur(root, 0, 0) 
        
        dic = [value for key,value in sorted(dic.items())]
        
        for i in range(len(dic)):
            dic[i].sort()
            for j in range(len(dic[i])):
                dic[i][j] =  dic[i][j][1]
        return dic
        