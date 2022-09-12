class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        
        def helper(array, d):
            
            sum = 0
            
            for i in array:
                
                sum += math.ceil(i/d)
                
            return sum
        
        
        left = 1
        right = 10**6
         
        while left <= right:
            
            mid = int(left + (right - left) / 2)
            
            result = helper(nums, mid)
            
            if result > threshold:
                
                left = mid + 1
               
            else:
                 right = mid - 1
              
                
        return left
            
            