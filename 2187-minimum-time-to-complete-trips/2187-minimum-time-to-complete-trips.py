class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = 10 ** 15
        
        def getTripsAt(sec):
            count = 0
            for i in range(len(time)):
                count += (sec // time[i])
            return count
    
        
        while l + 1 < r:
            mid = (l + r) // 2
            if getTripsAt(mid) >= totalTrips:
                r = mid
            else:
                l = mid
                
        return int(r)    
        
        
    
                
        
        