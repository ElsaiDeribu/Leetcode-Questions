class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # TC: O(n)
        # SC: O(n)

        ans = 0
        nums = set(nums)

        for num in nums:

            if num - 1 not in nums:
                count = 1
                curr = num

                while curr + 1 in nums:
                    curr += 1
                    count += 1
                
                ans = max(ans, count)


        return ans