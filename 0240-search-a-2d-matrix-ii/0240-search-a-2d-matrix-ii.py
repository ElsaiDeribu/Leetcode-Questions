class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = len(matrix) - 1
        c = 0

        
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            elif matrix[r][c] == target:
                return True
            
            
        # print("hello world")