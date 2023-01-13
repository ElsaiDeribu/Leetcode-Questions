class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

                    m = len(matrix)
                    n = len(matrix[0])
                    left = -1
                    right = m * n - 1


                    while left + 1 < right:
                        mid = (left + right) // 2

                        row = mid // n
                        col = mid % n

                        if matrix[row][col] >= target:
                            right = mid

                        else:
                            left = mid 


                    row = right // n
                    col = right % n

                    return matrix[row][col] == target

    
    
#         row = 0
#         col = len(matrix[0]) - 1
        
        
#         while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            
#             if matrix[row][col] > target:
#                 col -= 1
                
#             elif matrix[row][col] < target:
#                 row += 1
                
#             else:
#                 return True
            
#         return False
        
        
        
        
        
        
        
#         left = 0
#         right = len(matrix[0])
        
#         top = 0
#         bottom = len(matrix)
        
        
#         while left < right and bottom > top:
            
#             rowMid = left + right // 2
#             colMid = top + bottom // 2
            
#             if matrix[colMid][rowMid] >= target:
#                 right = rowMid
#                 bottom = colMid 
                
#             else:
                
#                 left = rowMid + 1
#                 top = colMid + 1

                
#         return True if (bottom < len(matrix) and right < len(matrix)) and  matrix[bottom][right] == target else False
                
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def binSearch(row):
#             l = -1
#             r = len(matrix[0])
#             while l + 1 < r:
#                 mid = (l + r) // 2
#                 if matrix[row][mid] >= target:
#                     r = mid
#                 else:
#                     l = mid
#             return True if matrix[row][r] == target else False
        
        
        
#         for i in range(len(matrix)):
#             if matrix[i][-1] >= target:
#                 return binSearch(i)
            
            
        
