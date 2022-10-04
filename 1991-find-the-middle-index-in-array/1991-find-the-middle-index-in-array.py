class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        pref = [0] * len(nums)
        suf = [0] * len(nums)   
        
        pref[0] = nums[0]
        suf[-1] = nums[-1]
        
        if len(nums) == 1 :
            return 0

        for i in range(1,len(nums)):
            
            pref[i] = pref[i - 1] + nums[i]
            
        for i in range(len(nums) - 2,-1, -1):
            
            suf[i] = suf[i + 1] + nums[i]
            
        
        for i in range(len(nums)):
            if i == 0:
                if suf[1] == 0:
                    return i
            if i == len(nums) - 1:
                if pref[i - 1] == 0:
                    return i
            
            if 0 < i < len(nums) - 1:
                if pref[i - 1] == suf[i + 1]:
                    return i
            
        return -1
            
            