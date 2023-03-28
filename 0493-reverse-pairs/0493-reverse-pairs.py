class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        count = 0
        
        def divide(arr):
            
            nonlocal count
            
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            
            l = 0
            r = 0
            
            while l < len(left):
                
                while r < len(right) and left[l] > (2 * right[r]):
                    r += 1
                
                count += r
                l += 1
                
            l = 0
            r = 0
            ptr = 0
            
            while l < len(left) or r < len(right):
                
                if r >= len(right) or (l < len(left) and left[l] < right[r]):
                    arr[ptr] = left[l]
                    l += 1
                    ptr += 1
                    
                else:
                    arr[ptr] = right[r]
                    r += 1
                    ptr += 1
                    
                    
            return arr
        
        divide(nums)
        
        return count
            
                    
                
            
            
            
            