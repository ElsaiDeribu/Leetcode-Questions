class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self. givenMatrix = matrix
        for i in range(len(self.givenMatrix)):
            for j in range(1, len(self.givenMatrix[i])):
                
                self.givenMatrix[i][j] += self.givenMatrix[i][j-1]
       

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        self.sum = 0

        for k in range(row1, row2 + 1):
            
            if col1 == 0 :
                self.sum += self.givenMatrix[k][col2]
                           
            else:
                self.sum += self.givenMatrix[k][col2] - (self.givenMatrix[k][col1 - 1 ])  
                 
        return self.sum               

                           
                           
                         
                           
                           
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)