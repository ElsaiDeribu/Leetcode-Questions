class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        left, right = 0, len(nums) - 1
        operationsCount = 0
        nums.sort()
        
        while left < right:
            
            total = nums[left] + nums[right]
            
            if total < k:
                left += 1
                
            elif total > k:
                right -= 1
                
            else:
                operationsCount += 1
                left += 1
                right -= 1
                
                
        return operationsCount
            
            
            
            
        