class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        
        
        direction = 'right'
        ans = []
        
        
        while left <= right and bottom >= top:
            
            if direction == 'right':
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                    
                top += 1
                direction = 'down'
                
            elif direction == 'down':
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                    
                right -= 1
                direction = 'left'
                
            elif direction == 'left':
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                                
                bottom -= 1
                direction = 'up'
                
            elif direction == 'up':

                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                
                left += 1
                direction = 'right'
                

        return ans
                
                
                    
                    
        
        
        
        