class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        
        start = bisect_left(nums, target)
        end = bisect_right(nums, target)
        
        start = start if 0 <= start < len(nums) and nums[start] == target else -1
        end = end - 1 if start != -1 else -1
        
        
        return [start, end]
        
        
        
                