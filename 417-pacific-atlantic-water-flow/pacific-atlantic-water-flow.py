class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       
        deq = deque([])
        visited = set()
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        def is_inbound(row, col):
            return 0 <= row < len(heights) and 0 <= col < len(heights[0])


        for col in range(len(heights[0])):
            visited.add((0,col))
            deq.append((0,col))

        for row in range(len(heights)):
            visited.add((row,0))
            deq.append((row,0))
        
        

        while deq:

            for _ in range(len(deq)):
                row, col = deq.popleft()

                for dr, dc in dirs:
                    new_row = dr + row
                    new_col = dc + col

                    if is_inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        if heights[new_row][new_col] >= heights[row][col]:
                            visited.add((new_row, new_col))
                            deq.append((new_row, new_col))



        deq = deque([])
        paci = visited.copy()
        visited = set()

        for col in range(len(heights[0])):
            visited.add((len(heights) - 1,col))
            deq.append((len(heights) - 1,col))

        for row in range(len(heights)):
            visited.add((row,len(heights[0]) - 1))
            deq.append((row,len(heights[0]) - 1))
        
        

        while deq:

            for _ in range(len(deq)):
                row, col = deq.popleft()

                for dr, dc in dirs:
                    new_row = dr + row
                    new_col = dc + col

                    if is_inbound(new_row, new_col) and (new_row, new_col) not in visited:
                        if heights[new_row][new_col] >= heights[row][col]:
                            visited.add((new_row, new_col))
                            deq.append((new_row, new_col))


        ans = []
        for item in visited:
            if item in paci:
                ans.append(list(item))

        return ans









        