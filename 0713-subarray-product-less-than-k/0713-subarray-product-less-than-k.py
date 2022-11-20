class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        subArrProd = 1
        l = 0
        count = 0
        for r in range(len(nums)):
            subArrProd *= nums[r]
            while l <= r and subArrProd >= k:
                subArrProd /= nums[l]
                l += 1
            if subArrProd < k:    
                count += (r - l + 1)
            
        return count
    
    
            
        