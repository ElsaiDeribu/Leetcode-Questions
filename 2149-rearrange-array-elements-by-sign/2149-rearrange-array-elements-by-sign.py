class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        ans = [0] * len(nums)
        
        
        j = 0
        k = 0
        
        for i in range(len(ans)):
            
            while j < len(ans) and nums[j] > 0:
                j += 1
                
            while k < len(ans) and nums[k] < 0:
                k += 1
                
                
            if i % 2 == 0:
                ans[i] = nums[k]
                k += 1
                
            else:
                ans[i] = nums[j]
                j += 1
        
        
        return ans
                
            
        
    