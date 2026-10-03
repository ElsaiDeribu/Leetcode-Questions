class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        ans = [1] * len(nums)

        running_prod = 1

        for i in range(len(nums)):
            ans[i] *= running_prod
            running_prod *= nums[i]
            

        running_prod = 1
        
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= running_prod
            running_prod *= nums[i]


        return ans
