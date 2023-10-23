class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        l = r = k 
        ans = nums[k]
        smallest = nums[k]
        
        while l > 0 or r < len(nums) - 1:
            
            if l == 0 or (r < len(nums) - 1 and nums[l - 1] < nums[r + 1]):
                r += 1
                smallest = min(smallest, nums[r])
                
            else:
                l -= 1 
                smallest = min(smallest, nums[l])
                
                
            ans = max(ans, smallest * (r - l + 1) )
            
            
        return ans
                
            
            
        
        
        

        
        