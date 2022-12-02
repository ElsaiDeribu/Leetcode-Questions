class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        # O(m + n) solution
        
#         r = len(matrix) - 1
#         c = 0
        
#         while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            
#             if matrix[r][c] > target:
#                 r -= 1
#             elif matrix[r][c] < target:
#                 c += 1
#             elif matrix[r][c] == target:
#                 return True
            
            
        
        
        # O(mlog(n) ) solution
        
        def binSearch(row):
            l = -1
            r = len(matrix[0])
            while l + 1 < r:
                mid = (l + r) // 2
                if matrix[row][mid] >= target:
                    r = mid
                else:
                    l = mid
            return matrix[row][r] if r != len(matrix[0]) else ""
            
            
        for i in range(len(matrix)):
            if binSearch(i) == target:
                return True
                
                
                
                
                