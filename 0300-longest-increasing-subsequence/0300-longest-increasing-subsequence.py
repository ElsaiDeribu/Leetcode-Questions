class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        lis = [1] * len(nums)
        
        for i in range(1, len(nums)):
            
            longest = 0
            for j in range(i):
                
                if nums[j] < nums[i] and lis[j] > longest:
                    longest = lis[j]
                    
            lis[i] = longest + 1
            
            
        return max(lis)
        