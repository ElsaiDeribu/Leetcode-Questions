class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        total = 0
        
        i = 0
        j = 1
        
        while j < len(nums):
            
            total += min(nums[i], nums[j])
            
            j += 2
            i += 2
            
        return total
        
        
        