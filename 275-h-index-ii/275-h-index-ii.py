class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        end = len(citations) - 1
        h = 0
        
        while start <= end:
            
            mid = start + (end - start) // 2
            
            if citations[mid] >= (len(citations) - mid):
                h = max(h, (len(citations) - mid) )
                end = mid - 1
                
            else:
                
                start = mid + 1
                
        return h