class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        prev_run_len = 0   
        curr_len = 1      
        ans = 1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                curr_len += 1
            else:
                prev_run_len = curr_len
                curr_len = 1

            if prev_run_len >= curr_len:
                ans = max(ans, curr_len)

            ans = max(ans, curr_len // 2)

        return ans
