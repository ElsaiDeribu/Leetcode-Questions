# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def build(start, end):
            if start > end:
                return [None]
            
            trees = []
            for i in range(start, end + 1):
                resLeft = build(start, i - 1)
                resRight = build(i + 1, end)
                for l in resLeft:
                    for r in resRight:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        trees.append(curr)
                
            return trees
        
        
        return build(1, n)
        
            