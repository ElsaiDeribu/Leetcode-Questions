class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        ans = 0
        
        for i in range(len(nums)):
            subMax = nums[i]
            subMin = nums[i]
            for j in range(i + 1, len(nums)):
                subMax = max(subMax, nums[j])
                subMin = min(subMin, nums[j])
                
                ans += (subMax - subMin)
            
        return ans

