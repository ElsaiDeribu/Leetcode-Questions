class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        largest = 0

        for i in range(len(nums) - 1):
            n = nums[i]
            largest = max(largest, n)

            if largest == 0:
                return False
                
            largest -= 1

        return True
    