class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums, reverse = True)
        ans = 0
        
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k :
                
                if nums[j] + nums[k] > nums[i]:
                    ans += (k - j)
                    j += 1

                    
                else:
                    
                    k -= 1

                    
        return ans 
        
        
        