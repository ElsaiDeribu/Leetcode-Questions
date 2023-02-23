class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        
        row, col = len(matrix), len(matrix[0])
        self.matrix = matrix

        for i in range(row):
            for j in range(col):
                self.matrix[i][j] += self.get_value(i-1, j) +  self.get_value(i, j - 1) -  self.get_value(i-1, j-1)
    
        
    def get_value(self, i, j):
        if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[0]):
            return self.matrix[i][j]
            
        return 0


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
                                               
         
        return self.matrix[row2][col2] - self.get_value(row2, col1 -1) - self.get_value(row1 - 1, col2) + self.get_value(row1 - 1, col1 - 1) 
                                            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)