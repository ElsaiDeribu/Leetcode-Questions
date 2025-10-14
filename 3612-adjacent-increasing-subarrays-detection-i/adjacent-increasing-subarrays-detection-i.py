class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        inc = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc[i] = inc[i - 1] + 1

        for i in range(len(nums) - k):

            if inc[i] >= k and inc[i + k] >= k:
                return True

        return False

        
        