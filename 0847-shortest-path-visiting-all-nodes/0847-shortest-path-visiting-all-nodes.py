class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:

        n = len(graph)
        target = (1 << n) - 1
        ans = float("inf")
        
        for i in range(n):
            deq = deque([(i, (1 << i))])
            seen = set((i, 1 << i))
            path = 0
            
            while deq:
                if any([b == target for _, b in deq]):
                    ans = min(ans, path)
                    break
                    
                path += 1
                
                for _ in range(len(deq)):
                    node, visited = deq.popleft()
                    for neighbour in graph[node] :
                            v = visited | (1 << neighbour)
                            if (neighbour, v) not in seen:
                                seen.add((neighbour, v))
                                deq.append((neighbour, v))
                     
        return ans
