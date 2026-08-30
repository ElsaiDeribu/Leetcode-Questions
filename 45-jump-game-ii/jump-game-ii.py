class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # TC: O(n)
        # SC: O(1)

        steps = 0
        left, right = 0, 0

        while right < len(nums) - 1:

            new_right = 0
            for idx in range(left, right + 1):
                new_right = max(idx + nums[idx], new_right)

            left = right + 1
            right = new_right
            steps += 1


        return steps
            



