class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                
                if nums[j] < nums[i]:
                    count += 1
                    
            ans[i] = count
            
            
            
        return ans