class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            nums[i] = (nums[i], i)

        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            res = nums[l][0] + nums[r][0]

            if res > target:
                r -= 1
            elif res < target:
                l += 1
            else:
                return [nums[l][1], nums[r][1]]
        