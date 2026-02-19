class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]


        def bisect_lft(target):

            l, r = 0, len(nums)

            while l < r:
                m = (l + r) // 2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m

            return l



        def bisect_rgt(target):

            l, r = 0, len(nums)

            while l < r:
                m = (l + r) // 2

                if nums[m] <= target:
                    l = m + 1
                else: 
                    r = m

            return l

        left = bisect_lft(target)
        right = bisect_rgt(target) - 1 
        
        if left > right:
            return [-1, -1]


        return [left, right]
