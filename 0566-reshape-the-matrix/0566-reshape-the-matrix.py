class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        
        reshapedMatrix = [[0] * c for i in range(r)]
        
        currImaginaryIndex = 0
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                rw = currImaginaryIndex // c
                cl = currImaginaryIndex % c
                
                reshapedMatrix[rw][cl] = mat[row][col]
                currImaginaryIndex += 1
        
        
        return reshapedMatrix
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         reshapedMatrix = [[0] * c for i in range(r)]
        
#         oneDimentionalMatrix = []
#         for row in mat:
#             oneDimentionalMatrix.extend(row)
        
#         oneDpointer = 0
        
#         for row in range(r):
#             for col in range(c):
#                 reshapedMatrix[row][col] = oneDimentionalMatrix[oneDpointer]
#                 oneDpointer += 1
                
                
#         return reshapedMatrix