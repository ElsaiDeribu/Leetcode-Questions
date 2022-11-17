class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        operations = 0
        l = 0
        r = len(nums) - 1
        
        
        while l < r:
            twoSum = nums[l] + nums[r]
            if twoSum > k:
                r -= 1
            elif twoSum < k:
                l += 1
            else:
                operations += 1
                l += 1
                r -= 1
                
        return operations
        
            
            
            
        
        