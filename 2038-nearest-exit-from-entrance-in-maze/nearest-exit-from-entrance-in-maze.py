class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        deq = deque([entrance])
        dir = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set((entrance[0], entrance[1]))
        steps = 0


        while deq:
            for i in range(len(deq)):
                r, c = deq.popleft()
                
                if [r,c] != entrance and ( r == len(maze) - 1 or c == len(maze[0]) - 1 or r == 0 or c == 0 ):
                    return steps

                for d_r, d_c in dir:
                    row, col = r + d_r, c + d_c

                    if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and  maze[row][col] == "." and (row, col) not in visited:
                        deq.append([row,col])
                        visited.add((row,col))



            steps += 1

        return -1




        