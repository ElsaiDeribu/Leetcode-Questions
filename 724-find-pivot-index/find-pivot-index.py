class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        nums = [0,*nums,0]
        post = sum(nums[1:])
        pref = 0

        for i in range(1,len(nums) - 1):
            post -= nums[i]

            if pref == post:
                return i - 1
            
            pref += nums[i]


        return -1


        