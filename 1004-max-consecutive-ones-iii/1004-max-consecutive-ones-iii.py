class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        i = j = 0
        ans = 0
        
        while j < len(nums):
            
            if nums[j] == 0 :
                k -= 1
                
            while k < 0:
                if nums[i] == 0:
                    k += 1
                
                i += 1
            
            ans = max(ans, j - i + 1)
            j += 1
          
        
        
        
        return ans
                
        