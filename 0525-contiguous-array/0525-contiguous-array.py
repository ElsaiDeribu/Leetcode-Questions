class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixes = defaultdict(int)
        sumUpToNow = 0
        longest = 0
        
        for i in range(len(nums)):
            sumUpToNow += 1 if nums[i] else -1
            if sumUpToNow == 0:
                longest = i + 1
            elif sumUpToNow in prefixes:
                longest = max(longest, i - prefixes[sumUpToNow])
            if sumUpToNow not in prefixes:
                prefixes[sumUpToNow] = i
                
        return longest
            
            