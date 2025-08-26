class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        k = 0
        l = 0
        ans = 0

        for r in range(len(nums)):

            if nums[r] != 1:
                k += 1

            while k > 1:
                if nums[l] != 1:
                    k -= 1
                l += 1

            ans = max(ans, r - l)

        return ans

            