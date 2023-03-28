class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        
        for i in range(len(nums1)):
            nums1[i] = (nums1[i] - nums2[i])
            
        count = 0
            
        def divide(arr):
            nonlocal count
            
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            
            
            l = len(left) - 1
            r = len(right) - 1
                
            
            while l >= 0:

                while r >= 0 and (left[l] <= right[r] + diff):
                    r -= 1

                count += ((len(right) - 1) - r)
                l -= 1
             
            
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
        
        divide(nums1)
        
        return count
            
        
        
        