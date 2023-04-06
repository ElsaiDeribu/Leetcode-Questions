class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        neighbours = [0] * (n + 1)
        lookupEdges = set()
        ans = float("-inf")
        
        for road in roads:
            lookupEdges.add(tuple(road))
            neighbours[road[0]] += 1
            neighbours[road[1]] += 1
            

        for i in range(len(neighbours)):
            for j in range(i + 1, len(neighbours)):
                
                temp = neighbours[i] + neighbours[j] 
                temp -= 1 if ((i, j) in lookupEdges) or ((j, i) in lookupEdges) else 0
                ans = max(ans, temp)

        return ans