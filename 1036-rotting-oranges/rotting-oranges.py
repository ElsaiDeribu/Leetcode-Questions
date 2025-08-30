class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        deq = deque([])
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        mins = 0
        fr_cnt = 0


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    deq.append((r,c))
                elif grid[r][c] == 1:
                    fr_cnt += 1

        def isinbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        while deq:

            for _ in range(len(deq)):
                r, c = deq.popleft()

                for d_r, d_c in dir:
                    row, col = r + d_r, c + d_c

                    if isinbound(row,col) and (row, col) not in visited and grid[row][col] == 1:
                        fr_cnt -= 1
                        visited.add((row, col))
                        deq.append((row,col))
            if deq:
                 mins += 1



        return -1 if fr_cnt > 0 else mins