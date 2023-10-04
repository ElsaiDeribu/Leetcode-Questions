class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def find(n, arr):
            
            if len(arr) == 2:
                return n * gcd(arr[0], arr[1])
                
            arr = list(arr)
            imax = float("-inf")
            
            for i in range(len(arr)):
                x = arr.pop(i)
                jmax = float("-inf")
                
                for j in range(len(arr)):
                    y = arr.pop(j)
                    jmax = max(jmax, (find(n + 1, tuple(arr))) +  (n * gcd(x, y)) )
                    arr.insert(j, y)
                    
                imax = max(imax, jmax)
                arr.insert(i, x) 
                
            return imax 
        
         
        return find(1, tuple(nums))
    
        