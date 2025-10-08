class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        total = 0
        ans = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total - nums[l] >= target:
                total -= nums[l]
                l += 1

            if total >= target:
                length = r - l + 1
                ans = min(ans, length)


        return ans if ans != float("inf") else 0
        