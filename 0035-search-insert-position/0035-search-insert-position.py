class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        
        while l + 1 < r :
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid 
            else:
                l = mid 
            
        return  r
        
        