class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)
        
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        
        def divide(arr):
            
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            
            left = divide(arr[:mid])
            right = divide(arr[mid:])
            
            l = 0
            r = 0
            
            while l < len(left):
                
                while r < len(right) and right[r][0] < left[l][0]:
                    r += 1
                    
                count[left[l][1]] += r
                l += 1
            
            ptr = 0
            l = 0
            r = 0
            
            while l < len(left) or r < len(right):
                
                if r >= len(right) or (l < len(left) and left[l][0] < right[r][0]):
                    arr[ptr] = left[l]
                    l += 1
                    ptr += 1
                    
                else:
                    arr[ptr] = right[r]
                    r += 1
                    ptr += 1
                
            return arr
        
        divide(nums)
 
        
        for i in range(len(nums)):
            nums[i] = count[i]
        
        return nums