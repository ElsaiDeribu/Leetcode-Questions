# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        
        l = 0
        r = mountain_arr.length()
        n = mountain_arr.length()
        
        while l + 1 < r : 
             
            m = l + (r - l) // 2
            middle = mountain_arr.get(m) 

            if middle > target or (0 < m - 1 and m + 1 < n and mountain_arr.get(m - 1) > middle > mountain_arr.get(m + 1)):
                r = m
                
            elif middle <= target :
                l = m
                
            if middle == target and (0 < m - 1 and m + 1 < n  and mountain_arr.get(m - 1) < middle > mountain_arr.get(m + 1)) :
                return m
            
        if mountain_arr.get(l) == target:
            return l

            
        l = 0 
        r = mountain_arr.length() 
        
        while l + 1 < r :
            
            m = l + (r - l) // 2
            if mountain_arr.get(m) > target or (0 < m - 1 and m + 1 < n and mountain_arr.get(m - 1) < mountain_arr.get(m) < mountain_arr.get(m + 1)):
                l = m
                
            elif mountain_arr.get(m) <= target:
                r = m
            

        if r < mountain_arr.length() and mountain_arr.get(r) == target:
            return r
            
        return -1
       
    
    
    
    