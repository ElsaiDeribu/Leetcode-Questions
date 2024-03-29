class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        srcColor = image[sr][sc]
        image[sr][sc] = color
        row = len(image)
        col = len(image[0])
        
        def dfs(r, c):
            visited.add((r,c))
            for i in dir:
                coord = (r + i[0], c + i[1])
                if (0 <= coord[0] < row and 0 <= coord[1] < col) and (coord not in visited) and image[coord[0]][coord[1]] == srcColor :
                    image[coord[0]][coord[1]] = color
                    dfs(coord[0], coord[1])
                            
        dfs(sr, sc)
        
        return image
        