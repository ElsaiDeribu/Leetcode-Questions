class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefixes = defaultdict(int)
        prefixes[0] = 1
        sumUpToNow = 0
        count = 0
        
        for i in range(len(nums)):
            sumUpToNow += nums[i]
            rem = sumUpToNow % k
            count += prefixes[rem]
            prefixes[rem] += 1
            
        return count
            
            
        