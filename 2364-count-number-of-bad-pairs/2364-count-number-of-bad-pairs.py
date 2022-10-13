class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        totalPairs = (len(nums)*(len(nums) - 1)) / 2
        
        prevPairs = defaultdict(int)
        
        goodPairs = 0
        
        
        for i in range(len(nums)):
            
            goodPairs += prevPairs[nums[i] - i]
            prevPairs[nums[i] - i] += 1
            
            
            
        return (int(totalPairs - goodPairs))
        
        