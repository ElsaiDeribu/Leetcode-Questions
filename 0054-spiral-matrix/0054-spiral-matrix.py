class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        t , l = 0, 0
        b = len(matrix) - 1
        r = len(matrix[0]) - 1 
        
        direction = 0 
        ans = []
        
        while t <= b and l <= r:
            if direction == 0:
                for i in range(l, r + 1):
                    ans.append(matrix[t][i])
                t += 1
                direction = 1

            elif direction == 1:
                for i in range(t, b + 1):
                    ans.append(matrix[i][r])
                r -= 1
                direction = 2
                    
            elif direction == 2:
                for i in range(r, l - 1, - 1):
                    ans.append(matrix[b][i])
                    
                b -= 1    
                direction = 3
                
            elif direction == 3:
                for i in range(b, t - 1, - 1):
                    ans.append(matrix[i][l])
                l += 1
                direction = 0
                    
        return ans