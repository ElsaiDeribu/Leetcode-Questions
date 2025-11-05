class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = defaultdict(lambda:defaultdict(float))

        for i in range(len(equations)):
            a, b = equations[i][0], equations[i][1]
            adj_list[a][b] = values[i]
            adj_list[b][a] = 1 / values[i]


        def dfs(curr, req, product, visited):
            
            if curr not in adj_list:
                return -1 
                
            visited.add(curr)

            if curr == req:
                return product


            for child in adj_list[curr]:
                if child not in visited: 
                    res = dfs(child, req, product * adj_list[curr][child], visited)

                    if res != -1:
                        return res

            return -1

        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, 1, set()))


        return ans





        
