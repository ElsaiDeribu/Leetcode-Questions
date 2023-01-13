class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        
        prefixes = defaultdict(int)
        prefixes[0] = 1
        currSum = 0
        count = 0
        
        for i in range(len(nums)):
            currSum += nums[i]
            count += prefixes[currSum - goal]
            prefixes[currSum] += 1
            
        return count
            
        