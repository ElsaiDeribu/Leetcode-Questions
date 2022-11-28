class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 0
        r = 10000001
        
        def findTimeTaken(speed):
            total = 0
            for i in range(len(dist)):
                total += math.ceil(dist[i] / speed) if i < len(dist) - 1 else dist[i] / speed
            return total
        
        
        while l + 1 < r:
            mid = (l + r) // 2
            
            if findTimeTaken(mid) > hour:
                l = mid
            else:
                r = mid
                
                
        return r if r != 10000001 else -1