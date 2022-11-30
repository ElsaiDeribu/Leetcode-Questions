class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l = -1
        r = len(citations)
        n = len(citations) - 1
        
        while l + 1 < r:
            mid = (l + r) //2 
        
            if n - mid + 1  > citations[mid]:
                l = mid
            else:
                r = mid
                
        return n - l 
        

                
        