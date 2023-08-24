class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        
        
        def getSum(idx):
            r, c = idx
            total = 0
            
            for row in range(max(0,r - k), min(len(mat), r + k + 1)):
                for col in range(max(0, c - k), min(len(mat[0]), c + k + 1)):
                    total += mat[row][col]
                    
            return total
            
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                ans[row][col] = getSum((row, col))
                
        return ans
                
                