class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
 
        pref = []
        post = []
        ans = []

        running_prod = 1
        for num in nums:
            running_prod *= num
            pref.append(running_prod)


        running_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            running_prod *= nums[i]
            post.append(running_prod)

        post = post[::-1]

        for i in range(len(nums)):
            if i == 0:
                ans.append(post[1])
            elif i == len(nums) - 1:
                ans.append(pref[-2])
            else:
                ans.append(pref[i - 1] * post[i + 1])

        return ans