class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        ans = []

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < target:
                l = m + 1
            else:
                r = m

        ans.append(r if nums[r] == target else -1)


        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] <= target:
                l = m + 1
            else:
                r = m - 1

        ans.append(l - 1 if nums[l - 1] == target else -1)

        return ans

        