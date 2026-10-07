class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1
        ans = []

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1

        if l < len(nums) and nums[l] == target:
            ans.append(l)
        else:
            return[-1, -1]


        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        ans.append(l - 1)


        return ans

