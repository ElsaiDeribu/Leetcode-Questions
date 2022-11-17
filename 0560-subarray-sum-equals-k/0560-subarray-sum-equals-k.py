class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        currSum = 0
        prefixes = defaultdict(int)
        prefixes[0] = 1
        count = 0
        
        for i in range(len(nums)):
            currSum += nums[i]
            count += prefixes[currSum - k]
            prefixes[currSum] += 1
            
        return count
        
                
            