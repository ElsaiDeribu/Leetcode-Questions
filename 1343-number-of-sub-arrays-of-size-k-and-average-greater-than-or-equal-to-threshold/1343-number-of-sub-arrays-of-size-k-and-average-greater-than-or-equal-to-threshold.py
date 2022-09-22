class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        count = 0
        i = 0
        j = k - 1
        
        initialSum =  sum(arr[0:k])
        
        while j < len(arr)  :
            if (initialSum / k) >= threshold: 
                count += 1
                
            initialSum -= arr[i]
            i += 1
            j += 1
            if j < len(arr):
                initialSum += arr[j]
        
        return count
        
        

        