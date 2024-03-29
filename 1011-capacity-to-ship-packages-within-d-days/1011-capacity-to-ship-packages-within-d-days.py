class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        
        def takesTooManyDays(cap):
            d = 1
            subtot = 0
            for i in range(len(weights)):
                subtot += weights[i]
                if subtot > cap:
                    d += 1
                    subtot = weights[i]
                  
            return d 
        

        while l <= r:
            mid = (l + r) // 2
            
            if takesTooManyDays(mid) > days:
                l = mid + 1
            else:
                r = mid - 1
                
        return r + 1