# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def build(arr):
            if len(arr) == 0:
                return [None]
            
            trees = []
            for i in range(len(arr)):
                resLeft = build(arr[:i])
                resRight = build(arr[i + 1:])
                for l in resLeft:
                    for r in resRight:
                        curr = TreeNode(arr[i])
                        curr.left = l
                        curr.right = r
                        trees.append(curr)
                
            return trees
        
        arr = [i for i in range(1, n + 1)]
        
        return build(arr)
        
            