class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        ans = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    ans += 1
                    
                    
        return ans
        