class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def setElementsZero(index, direction):
            
            row = index[0]
            col = index[1]
            
            while 0 <= row < len(matrix)  and 0 <= col < len(matrix[0]):
                matrix[row][col] = 0
                row += direction[0]
                col += direction[1]
        
        indexesToSpread = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    indexesToSpread.append((row, col))
                    
                    
        for index in indexesToSpread:
            for direction in directions:
                setElementsZero(index, direction)
                    
          
