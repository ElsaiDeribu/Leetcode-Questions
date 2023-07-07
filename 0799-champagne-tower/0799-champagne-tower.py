class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        
        mat = [[0] * i for i in range(1, query_row + 2)]
        mat[0][0] += poured
        
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] > 1:
                    extra = mat[row][col] - 1
                    mat[row][col] = 1
                    
                    if row + 1 < len(mat):
                        mat[row + 1][col] += extra / 2
                        mat[row + 1][col + 1] += extra / 2
                         
        return mat[query_row][query_glass]
                
        
            