class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        ans = [0] * len(nums)
        
        even = 0
        odd = 1
        
        for i in range(len(nums)):
            
            if not (nums[i] % 2):
                ans[even] = nums[i]
                even += 2
                
            else:
                ans[odd] = nums[i]
                odd += 2
                
        return ans
            
        