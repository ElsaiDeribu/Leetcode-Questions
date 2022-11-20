class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        prefixes = defaultdict(int)
        prefixes[0] = 1
        sumUpToNow = 0
        count = 0
        
        for i in range(len(arr)):
            sumUpToNow  += arr[i]
            
            if sumUpToNow % 2 in prefixes:
                count += prefixes[sumUpToNow % 2]
                
            prefixes[sumUpToNow % 2] += 1
            
        n = len(arr)
        totalSub = n * (n + 1) / 2
        
        return int(totalSub - count) % (10**9 + 7)
        
        
                

                
                
        