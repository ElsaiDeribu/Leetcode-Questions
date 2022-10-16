class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        elements = set(nums)
        count = 1
        ans = 1
        
        if len(nums) == 0:
            return 0
        
        for i in range(len(nums)):
            n = nums[i]
            count = 1
            if n - 1 not in elements:
                while n + 1 in elements:
                    count += 1
                    n += 1

            ans = max(ans, count)
        
        return ans
                
            
        
        