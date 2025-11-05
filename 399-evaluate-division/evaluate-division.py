class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            adj_list[a][b] = val
            adj_list[b][a] = 1 / val


        def dfs(curr, target, visited):

            if curr == target:
                return 1

            visited.add(curr)

            for nebr, val  in adj_list[curr].items():
                if nebr not in visited: 
                    res = dfs(nebr, target, visited)

                    if res != -1: return res * val

            return -1


        ans = []

        for a, b in queries:
            if a not in adj_list or b not in adj_list:
                ans.append(-1)
            else:
                ans.append(dfs(a, b, set()))


        return ans





        
