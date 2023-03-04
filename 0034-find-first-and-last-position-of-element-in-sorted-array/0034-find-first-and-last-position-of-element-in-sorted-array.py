class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        left = -1
        right = len(nums) - 1
        
        
        while left + 1 < right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid
                
            else:
                left = mid
        
        first = right if nums[right] == target else -1
        
        
        left = 0
        right = len(nums) 
        
        
        while left + 1 < right:
            
            mid = left + (right - left) // 2
            
            if nums[mid] <= target:
                left = mid
                
            else:
                right = mid
        
        second = left if nums[left] == target else -1
        
        
        return [first, second]
        
        
            
            