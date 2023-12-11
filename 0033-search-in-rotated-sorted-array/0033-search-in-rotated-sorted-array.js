class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                
                l = mid + 1
            else:
                r = mid
                
            
        left = bisect_left(nums, target, lo = 0, hi = r - 1 )
        right = bisect_left(nums, target, lo = r, hi= len(nums) - 1)
        
        if left < len(nums) and nums[left] == target:
            return left
        
        if right < len(nums) and nums[right] == target:
            return right
        
        
        return -1
        
        
        
        
        