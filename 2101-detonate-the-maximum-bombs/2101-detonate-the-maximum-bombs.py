class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        adjList = [[] for i in range(len(bombs))]
      
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    distance = sqrt((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2)
                    rad = bombs[i][2] 

                    if distance <= rad:
                        adjList[i].append(j)
    
        
        maxBom = 1
        exploded = set()
        
        def explode(index):
            exploded.add(index)

            total = 1
            for idx in adjList[index]:
                if idx not in exploded:
                    total += explode(idx)
                    
            return total
        
        
        
        for i in range(len(adjList)):
            maxBom = max(maxBom, explode(i))
            exploded = set()
        

        return maxBom