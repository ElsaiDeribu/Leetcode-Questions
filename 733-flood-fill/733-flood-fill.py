class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        
        visited = set()
        prevColor = image[sr][sc]
        image[sr][sc] = newColor
        row = len(image)
        col = len(image[0])
        
        def dfs(row, col, prevColor, newColor, visited, image, r, c):
            visited.add((r,c))
            for i in dir:
                coord = (r + i[0], c + i[1])
                if 0 <= coord[0] < row and 0 <= coord[1] < col:
                    if coord not in visited and image[coord[0]][coord[1]] == prevColor :
                        image[coord[0]][coord[1]] = newColor
                        dfs(row, col, prevColor, newColor, visited, image, coord[0], coord[1])
                            
            
        dfs(row, col, prevColor, newColor, visited, image, sr, sc)
        
        return image