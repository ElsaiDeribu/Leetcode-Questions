class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        dis = len(set(nums))
        ans = 0
        
        for i in range(len(nums)):
            subEl = set()
            for j in range(i, len(nums)):
                subEl.add(nums[j])
                
                if len(subEl) == dis:
                    ans += 1
                    
                    
        return ans
                    
                
                

        