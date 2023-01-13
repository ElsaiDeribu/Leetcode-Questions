class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        prefixes = defaultdict(int)
        prefixes[0] = 1
        
        currSum = 0
        count = 0
        
        for i in arr:
            currSum += i
            rem = currSum % 2
            count += prefixes[1 - rem]
            prefixes[rem] += 1
        
        mod = 10 ** 9 + 7
        
        return count % mod
            
            