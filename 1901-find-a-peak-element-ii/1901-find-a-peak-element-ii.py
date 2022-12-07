class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        
        
        s = 0
        e = len(mat) - 1
        
        
        while s < e:
            mid = (s + e) // 2
            
            midColMaxIndex = mat[mid].index(max(mat[mid]))
            # print(mat[mid])
            # print(max(mat[mid]))
            # print(mid, midColMaxIndex)
            
            if mat[mid][midColMaxIndex] < mat[mid + 1][midColMaxIndex]:
                s = mid + 1
            else:
                e = mid
                
        return [s, mat[mid].index(max(mat[mid]))]
            