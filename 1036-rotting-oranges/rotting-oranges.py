class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        deq = deque([])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    deq.append((row, col))

        time = 0 if not deq else -1
        while deq:

            for _ in range(len(deq)):
                row, col = deq.popleft()

                for dr, dc in dirs:
                    new_row = row + dr
                    new_col = col + dc

                    if is_inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        deq.append((new_row, new_col))

            time += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        return time
