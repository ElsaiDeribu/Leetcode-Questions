class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        ans = 10**6
        l = 0
        r = k - 1
        subArrMin = nums[l]
        subArrMax = nums[r]
       
        while r < len(nums):
            ans = min(ans, subArrMax - subArrMin)
            r += 1
            if r < len(nums):
                subArrMax = nums[r]
            l += 1
            if l < len(nums):
                subArrMin = nums[l]
            
        return ans
            
            