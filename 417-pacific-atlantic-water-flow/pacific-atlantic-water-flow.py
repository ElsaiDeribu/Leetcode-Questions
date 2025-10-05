class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        p_visited = set()
        deq = deque()
        direc = [(0,1), (1,0), (-1,0), (0,-1)]

        def inbound(r,c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0])


        for r in range(len(heights)):
            deq.append((r,0))
            p_visited.add((r,0))

        for c in range(len(heights[0])):
            deq.append((0,c))
            p_visited.add((0,c))

        
        while deq:

            for _ in range(len(deq)):
                cell = deq.popleft()

                for r, c in direc:
                    row, col = cell[0] + r, cell[1] + c

                    if (row, col) not in p_visited and inbound(row, col) and heights[row][col] >= heights[cell[0]][cell[1]]:
                        p_visited.add((row,col))
                        deq.append((row,col))


        
        a_visited = set()

        for r in range(len(heights)):
            c = len(heights[0]) - 1
            deq.append((r,c))
            a_visited.add((r,c))

        for c in range(len(heights[0])):
            r = len(heights) - 1
            deq.append((r,c))
            a_visited.add((r,c))

        
        while deq:

            for _ in range(len(deq)):
                cell = deq.popleft()

                for r, c in direc:
                    row, col = cell[0] + r, cell[1] + c

                    if (row, col) not in a_visited and inbound(row, col) and heights[row][col] >= heights[cell[0]][cell[1]]:
                        a_visited.add((row,col))
                        deq.append((row,col))




        return list(p_visited & a_visited)







        