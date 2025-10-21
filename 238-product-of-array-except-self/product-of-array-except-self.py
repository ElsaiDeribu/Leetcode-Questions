class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = [1] * len(nums)
        pref[0] = nums[0]

        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i]

        post = [1] * len(nums)
        post[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]


        for i in range(len(nums)):
            if i == 0:
                nums[i] = post[i + 1]

            elif i == len(nums) - 1:
                nums[i] = pref[i - 1]

            else:
                nums[i] = pref[i - 1] * post[i + 1]


        return nums


        

        