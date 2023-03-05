class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        def revers(end):
            left = 0
            right = end
            
            while left < right:
                
                arr[right], arr[left] = arr[left], arr[right]
                
                left += 1
                right -= 1
        
        
        def findMaxIdx(end):
            maxIdx = 0
            for i in range(end + 1):
                if arr[i] > arr[maxIdx]:
                    maxIdx = i
                    
            return maxIdx
        
        
        ptr = len(arr) - 1
        
        ans = []
        
        while ptr > 0:
            
            maximum = findMaxIdx(ptr)
            
            ans.append(maximum + 1)
            ans.append(ptr + 1)
            
            revers(maximum)
            revers(ptr)
            
            ptr -= 1
            
        return ans