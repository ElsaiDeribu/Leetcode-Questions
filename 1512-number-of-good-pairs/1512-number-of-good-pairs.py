class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        prev = defaultdict(int)
        count = 0
        
        for i in range(len(nums)):
            count += prev[nums[i]]
            prev[nums[i]] += 1
            
        return count
            
    
                
        