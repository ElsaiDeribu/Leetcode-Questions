class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # TC: O(n)
        # SC: O(1)

        tank = nums[0]

        for i in range(len(nums) - 1):
            tank = max(nums[i], tank)
            if tank == 0: return False
            tank -= 1


        return True