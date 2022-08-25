class Solution:
    def hIndex(self, citations: List[int]) -> int:
        right = len(citations) - 1
        left = 0
        h = 0
        
        while left <= right:
            mid = left+(right - left) // 2
            
            if citations[mid] >= len(citations) - mid:
                right = mid - 1 
                h = max(h, len(citations) - mid )
            else:
                left = mid + 1
                
        return h
                
        
        