class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binSearch(row):
            l = -1
            r = len(matrix[0])
            while l + 1 < r:
                mid = (l + r) // 2
                if matrix[row][mid] >= target:
                    r = mid
                else:
                    l = mid
            return True if matrix[row][r] == target else False
        
        
        
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                return binSearch(i)
            
            
        