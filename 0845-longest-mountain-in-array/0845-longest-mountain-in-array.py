class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        longest = 0
        
        
        for i in range(1, len(arr) - 1):
            
            if arr[i - 1]  < arr[i] > arr[i + 1]:
                
                j = i
                while j > 0 and arr[j - 1] < arr[j]:
                    j -= 1
                 
                k = i
                while  k  < len(arr) - 1 and arr[k] > arr[k + 1]:
                    k += 1
                    
                longest = max(longest, k - j + 1 )
                
                
                
        return longest
                
        
        
        
        
     