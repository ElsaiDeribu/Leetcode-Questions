class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        pref_prod = [1] * len(nums)
        post_prod = [1] * len(nums)

        running_prod = 1

        for i in range(len(nums)):

            pref_prod[i] = running_prod
            running_prod *= nums[i]
            

        running_prod = 1
        
        for i in range(len(nums) - 1, -1, -1):
            post_prod[i] = running_prod
            running_prod *= nums[i]

        for i in range(len(nums)):
            nums[i] = pref_prod[i] * post_prod[i]


        return nums
