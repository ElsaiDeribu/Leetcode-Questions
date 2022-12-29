class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        ans = []  
        
        def traverseDiagonally(strtIndex, direction):
            temp = []
            r = 1
            c = -1
            row = strtIndex[0]
            col = strtIndex[1]
                
            while 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                temp.append(mat[row][col])
                row += r
                col += c
                
            return temp[::direction]
        
        print(traverseDiagonally((0,1),1))
        
        for i in range(len(mat[0])):
            direction = 1 if i % 2 else -1
            ans.extend(traverseDiagonally((0, i), direction))
            
        for j in range(1, len(mat)):
            direction = 1 if (j + (len(mat[0]) - 1)) % 2 else -1
            
            ans.extend(traverseDiagonally((j, len(mat[0]) - 1), direction))


        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            