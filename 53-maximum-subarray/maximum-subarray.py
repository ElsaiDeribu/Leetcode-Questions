class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        pref_sum = []
        total = 0

        for num in nums:
            total += num
            pref_sum.append(total)

        ans = float("-inf")
        running_min = 0

        for num in pref_sum:
            ans = max(ans, num - running_min )
            running_min = min(running_min, num)

        
        return ans