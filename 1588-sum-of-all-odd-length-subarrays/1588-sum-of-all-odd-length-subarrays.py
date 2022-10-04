class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        pref = [0] * len(arr)
        pref[0] = arr[0]
        total = sum(arr)
        
        
        for i in range(1, len(arr)):
            pref[i] = pref[i - 1] + arr[i]
            
            
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
               
                length = (j - i) + 1
                if length % 2 != 0 and i != 0:
                    subtotal = pref[j] - pref[i - 1]
                    total += subtotal
                    
                elif length % 2 != 0:
                    subtotal = pref[j]
                    total += subtotal
                    
        return total
                
        