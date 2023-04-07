class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        entering = set()
        ans = set()
        
        for edge in edges:
            entering.add(edge[1])
            
        
        for edge in edges:
            if edge[0] not in entering:
                ans.add(edge[0])
                
            if edge[1] not in entering:
                ans.add(edge[1])
                
        return ans
            
        