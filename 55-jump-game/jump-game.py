class Solution:
    def canJump(self, nums: List[int]) -> bool:

        furthest_I_can_go = 0

        for i in range(len(nums) - 1):

            furthest_I_can_go = max(furthest_I_can_go, nums[i])

            if furthest_I_can_go == 0:
                return False

            furthest_I_can_go -= 1

        return True





        