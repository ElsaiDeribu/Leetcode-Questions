class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        ops = 0
        cables = 0
        adj_list = defaultdict(list)
        visited = set()

        for n1, n2 in connections:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
            cables +=1

        if cables < n - 1: return -1


        def dfs(node):
            visited.add(node)

            for neigbr in adj_list[node]:
                if neigbr not in visited:
                    dfs(neigbr)


        for node in range(n):
            if node not in visited:
                ops +=1
                dfs(node)


        return ops - 1






        