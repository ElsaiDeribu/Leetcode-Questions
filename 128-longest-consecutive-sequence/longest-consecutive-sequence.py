class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        ans = 0

        for num in nums:

            if num - 1 not in nums:
                count = 1
                current = num

                while current + 1 in nums:
                    count += 1
                    current += 1

                ans = max(ans, count)


        return ans
        