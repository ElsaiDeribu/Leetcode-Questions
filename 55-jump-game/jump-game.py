class Solution:
    def canJump(self, nums: List[int]) -> bool:

        curr = nums[0]

        for i in range(len(nums)):
            
            if curr < 0:
                return False
                
            curr = max(curr, nums[i])
            curr -= 1



        return True
        