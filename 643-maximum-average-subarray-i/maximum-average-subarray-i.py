class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        avg = -float("inf")
        total = 0
        l = 0

        for r in range(len(nums)):

            total += nums[r]

            if r - l + 1 < k:
                continue

            avg = max(avg, total/k)

            total -= nums[l]
            
            l += 1

        return avg
                


        