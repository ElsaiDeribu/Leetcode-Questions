class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        
        for i in range(len(matrix[0])):
            col = i
            row = 0
            standard = matrix[row][col]
            
            while col < len(matrix[0]) and row < len(matrix):
                
                if matrix[row][col] != standard:
                    return False
                
                col += 1
                row += 1
                
        for i in range(1, len(matrix)):
            row = i
            col = 0
            standard = matrix[row][col]
            while col < len(matrix[0]) and row < len(matrix):
              
                if matrix[row][col] != standard:
                    return False
                
                row += 1
                col += 1
                
                
        return True
                
        