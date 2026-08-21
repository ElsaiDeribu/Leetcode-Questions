class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        ans = float("-inf")
        running_min = 0
        total = 0

        for num in nums:
            total += num
            ans = max(ans, total - running_min )
            running_min = min(running_min, total)

        
        return ans