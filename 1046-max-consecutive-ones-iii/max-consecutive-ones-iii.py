class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l = 0
        ans = 0

        for r in range(len(nums)):

            if nums[r] != 1:
                k -= 1

            while k < 0:
                if nums[l] != 1:
                    k += 1
                l += 1


            ans = max(ans, r - l + 1)


        return ans
        