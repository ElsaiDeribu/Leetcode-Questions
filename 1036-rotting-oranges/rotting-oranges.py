class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        deq = deque([])
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        mins = 0


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    deq.append((r,c))

        def isinbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        while deq:

            for _ in range(len(deq)):
                r, c = deq.popleft()

                for d_r, d_c in dir:
                    row, col = r + d_r, c + d_c

                    if isinbound(row,col) and (row, col) not in visited and grid[row][col] == 1:
                        grid[row][col] = 2
                        visited.add((row, col))
                        deq.append((row,col))
            if deq:
                 mins += 1



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1

        return mins