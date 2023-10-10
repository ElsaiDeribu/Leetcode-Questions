class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(set(nums))
        ans = float("inf")
        
        for i in range(len(nums)):
            right = bisect_right(nums, nums[i] + n - 1)
            ans = min(ans, n - (right - i))
            
            
        return ans
            
        