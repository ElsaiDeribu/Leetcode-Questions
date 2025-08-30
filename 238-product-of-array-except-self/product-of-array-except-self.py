class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = [1 for _ in range(len(nums))]
        post = [1 for _ in range(len(nums))]

        for i in range(len(nums)):

            if i == 0:
                pref[i] = nums[i]
                continue

            pref[i] = pref[i - 1] * nums[i]

        for i in range(len(nums) - 1, -1, -1):

            if i == len(nums) - 1:
                post[i] = nums[i]
                continue

            post[i] = post[i + 1] * nums[i]


        for i in range(len(nums)):
            if i == 0:
                nums[i] = post[i + 1]
                continue

            if i == len(nums) - 1:
                nums[i] = pref[i - 1]
                continue
                
            nums[i] = pref[i - 1] * post[i + 1]


        return nums

            
        



            
        
