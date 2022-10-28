class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        
        
        diagonals = []
        for i in range(len(mat) - 1, 0, -1 ):
            temp = []
            r = i
            c = 0
            
            while r < m and c < n:
                temp.append(mat[r][c])
                r += 1
                c += 1
            diagonals.append(sorted(temp))
          
        
        for i in range(len(mat[0])):
            temp = []
            r = 0
            c = i
            
            while r < m and c < n:
                temp.append(mat[r][c])
                r += 1
                c += 1
            diagonals.append(sorted(temp))
        
        
        replacementRow = 0
        
        for i in range(len(mat) - 1, 0, -1 ):
            replacementCol = 0
            r = i
            c = 0
            
            while r < m and c < n:
                mat[r][c] = diagonals[replacementRow][replacementCol]
                r += 1
                c += 1
                replacementCol += 1
            
            replacementRow += 1
            
            
            
        for i in range(len(mat[0])):
            replacementCol = 0
            r = 0
            c = i
            
            while r < m and c < n:
                mat[r][c] = diagonals[replacementRow][replacementCol]
                r += 1
                c += 1
                replacementCol += 1
                
            replacementRow += 1            
            
        return mat             
 
        