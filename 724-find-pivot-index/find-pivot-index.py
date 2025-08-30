class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
        pref = 0

        for i in range(len(nums)):

            if pref == total - pref - nums[i]:
                return i 
            
            pref += nums[i]


        return -1


        