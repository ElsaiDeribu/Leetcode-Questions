class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        inc = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc[i] = inc[i - 1] + 1

        print(inc)
        ans = 1
        for i in range(len(nums)):
            k = inc[i]

            if i - k >= 0 and inc[i] <= inc[i - k]:
                ans = max(ans, k)
                
            ans = max(ans, k//2)


        return ans
        