class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        new_pos = {}

        for i, num in enumerate(nums):
            new_pos[(i + k) % len(nums)] = num

        for key, value in new_pos.items():
            nums[key] = value
