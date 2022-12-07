class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0] * n for i in range(n)]
        t , l = 0, 0
        b = n - 1
        r = n - 1 
        
        direction = 0 
        element = 1
        
        while t <= b and l <= r:
            if direction == 0:
                for i in range(l, r + 1):
                    matrix[t][i] = element
                    element += 1
                t += 1
                direction = 1
                

            elif direction == 1:
                for i in range(t, b + 1):
                    matrix[i][r] = element
                    element += 1
                r -= 1
                direction = 2
                    
            elif direction == 2:
                for i in range(r, l - 1, - 1):
                    matrix[b][i] = element
                    element += 1
                    
                b -= 1    
                direction = 3
                
            elif direction == 3:
                for i in range(b, t - 1, - 1):
                    matrix[i][l] = element
                    element += 1
                l += 1
                direction = 0
                
                    
        return matrix
        