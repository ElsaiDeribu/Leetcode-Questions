class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        first = bisect_left(nums, target)
        
        first = first if first < len(nums) and nums[first] == target else -1
        
        second = bisect_right(nums, target)
        
        second = second - 1 if nums[second - 1] == target else -1
        
        return [first, second]
        
        
            
            