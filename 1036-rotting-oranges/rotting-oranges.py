class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # TC: O(m * n)
        # SC: O(m * n)
        
        deq = deque([])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    deq.append((row, col))

        time = -1 if deq else 0 # -1 if we have rotten oranges at the start since they don't take time to rot
        while deq:
            for _ in range(len(deq)):

                row, col = deq.popleft()
               
                for dr, dc in dirs:
                    new_row = dr + row
                    new_col = dc + col
                    if is_inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        deq.append((new_row, new_col))
            time += 1


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1


        return time