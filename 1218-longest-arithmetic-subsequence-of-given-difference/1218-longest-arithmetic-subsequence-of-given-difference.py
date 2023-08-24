class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        
        prev = defaultdict(int)
        
        for i in range(len(arr)):
            prev[arr[i]] = prev[arr[i] - difference] + 1
            
        return max(prev.items(), key= lambda x : x[1])[1] 
            
        
        
        