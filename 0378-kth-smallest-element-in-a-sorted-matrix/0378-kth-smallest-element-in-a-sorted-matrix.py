class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        
        
        
        
        
        
        # Sorting solution
        elements = []
        for i in matrix:
            elements.extend(i)
                
        elements.sort()
        return elements[k - 1]
