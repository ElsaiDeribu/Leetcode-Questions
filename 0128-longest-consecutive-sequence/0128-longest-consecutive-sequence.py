class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        count = 1
        ans = 1
        
        if len(nums) == 0:
            return 0
        
        for i in nums:
            n = i
            count = 1
            if n - 1 not in nums:
                while n + 1 in nums:
                    count += 1
                    n += 1

            ans = max(ans, count)
        
        return ans
                
            
        
        