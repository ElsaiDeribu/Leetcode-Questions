class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        a = float("-inf")
        b = float("inf")
        ans = 1
        
        for num in nums:
            if num > a:
                a = num
            if num < b:
                b = num
          
        return self.gcd(a, b)
    
    
    def gcd(self, a, b):
        if b == 0:
            return a
        
        return gcd(b, a % b)
                
            
            
            
    