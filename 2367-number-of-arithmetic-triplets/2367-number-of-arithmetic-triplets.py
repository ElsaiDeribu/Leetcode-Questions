class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        count = 0
        
        visited = set()
        
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        count += 1
                        
        return count
                    
                    
                
                    
                
            
        