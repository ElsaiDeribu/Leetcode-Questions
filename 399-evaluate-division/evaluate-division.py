from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        # Build graph: adjacency list with weights
        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(curr, target, visited, acc):
            if curr == target:
                return acc
            visited.add(curr)

            for nei, val in graph[curr].items():
                if nei not in visited:
                    res = dfs(nei, target, visited, acc * val)
                    if res != -1:
                        return res
            return -1

        
        for i in range(len(queries)):
            a, b = queries[i][0], queries[i][1]
    
            if a not in graph or b not in graph:
                queries[i] = -1.0
            else:
                queries[i] = dfs(a, b, set(), 1.0)

        return queries
