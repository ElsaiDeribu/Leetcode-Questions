# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        
        def findDepth(node):
            if not node:
                return 0
            
            leftDepth = findDepth(node.left)
            rightDepth = findDepth(node.right)
            
            return max(leftDepth, rightDepth) + 1
        
        graphHeight = findDepth(root)
        graphWidth = 2 ** graphHeight - 1
        
        matrix = [[""] * graphWidth for i in range(graphHeight)]
        
        
        def buildMatrix(grid, node, currRow, left, right):
            
            if not node:
                return 
            
            mid = (left + right) // 2
            
            grid[currRow][mid] = str(node.val)
            
            buildMatrix(grid, node.left, currRow + 1, left, mid - 1)
            buildMatrix(grid, node.right, currRow + 1, mid + 1, right )
        
        buildMatrix(matrix, root, 0, 0, len(matrix[0]))
        
        return matrix