class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        count = 0
        subProd = 1
        
        l = r = 0
        
        while r < len(nums):
            
            subProd *= nums[r]
            
            while l <= r and subProd >= k:
                subProd /= nums[l]
                l += 1
                
            count += (r - l + 1)
            
            r += 1
            
            
        return count
                
            
        