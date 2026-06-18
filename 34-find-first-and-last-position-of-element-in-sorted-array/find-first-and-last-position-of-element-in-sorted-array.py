class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        left = bisect_left(nums, target)

        if not (left < len(nums) and nums[left] == target):
            return [-1, -1]

        right = bisect_right(nums, target) - 1

        return [left, right]

