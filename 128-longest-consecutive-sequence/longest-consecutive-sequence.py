class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        cons_nums = set(nums)
        ans = 0

        for num in cons_nums:

            if num - 1 not in cons_nums:
                count = 1
                nxt = num

                while nxt + 1 in cons_nums:
                    count += 1
                    nxt += 1

                ans = max(ans, count)

        return ans



        