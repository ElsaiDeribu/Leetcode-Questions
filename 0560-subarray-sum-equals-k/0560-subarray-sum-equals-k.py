class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixes = defaultdict(int)
        prefixes[0] = 1
        sumUpToNow = 0
        count = 0
        
        for i in range(len(nums)):
            sumUpToNow += nums[i]
            if prefixes[sumUpToNow - k] > 0:
                count += prefixes[sumUpToNow - k]
                
            prefixes[sumUpToNow] += 1
            
        return count
                
            