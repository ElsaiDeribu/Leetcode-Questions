# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start = 1
        end = n
        
        if isBadVersion(start):
            return start
        
        while start != (end - 1):
            
            middle = math.ceil((start + end)/2)
            
            if isBadVersion(middle):
                end = middle 
            else:
                start = middle 
        
        return end
            
            
        