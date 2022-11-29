class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        l = 0
        r = 10000001
        
        def numCh(n):
            total = 0
            for i in range(len(candies)):
                total += candies[i] // n
            return total
        
        
        while l + 1 < r:
            mid = (l + r) // 2
            if numCh(mid) >= k:
                l = mid
            else:
                r = mid
                
        return l
                