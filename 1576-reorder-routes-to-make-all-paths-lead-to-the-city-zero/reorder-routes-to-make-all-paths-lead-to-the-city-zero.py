class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        neighbours = defaultdict(set)
        visited = set()
        conn = {(s, e) for s, e in connections}
        self.ans = 0

        for a, b in connections:
            neighbours[a].add(b)
            neighbours[b].add(a)


        def dfs(curr):
            
            visited.add(curr)
            for n in neighbours[curr]:
                if n not in visited:
                    if (n,curr) not in conn:
                        self.ans += 1

                    dfs(n)


        
        dfs(0)



        return self.ans





        
        
