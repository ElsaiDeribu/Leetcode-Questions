class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
 
        ans = []

        running_prod = 1
        for num in nums:
            ans.append(running_prod)
            running_prod *= num


        running_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= running_prod
            running_prod *= nums[i]


        return ans