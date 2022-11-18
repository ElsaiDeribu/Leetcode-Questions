class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        
        for i in range(len(nums)):
            if nums[i] % 2 :
                nums[i] = 1
            else:
                nums[i] = 0
                
        prefixes = defaultdict(int)
        prefixes[0] = 1
        count = 0
        sumUpToNow = 0
        
        for i in range(len(nums)):
            sumUpToNow += nums[i]
            count += prefixes[sumUpToNow - k]
            prefixes[sumUpToNow] += 1
            
        return count
            
        
        
        
        