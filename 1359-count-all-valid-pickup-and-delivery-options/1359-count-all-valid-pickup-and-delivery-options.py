class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        MOD = 10**9 + 7
        x = n * 2
        totalWays = 1
        
        for _ in range(n):
            
            totalWays *= (x * (x - 1)) / 2 
            totalWays %= MOD
            
            x -= 2
            
        return totalWays
        
        