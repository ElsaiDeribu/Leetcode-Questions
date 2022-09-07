class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLeft(nums):
            
            start, end, index = 0, len(nums) - 1, -1
            
            while start <= end:
                
                mid = start + (end - start) // 2
                
                if nums[mid] >= target:
                    
                    end = mid - 1 
                    
                else: 
                    start = mid + 1
                    
                if nums[mid] == target:
                    
                    index = mid
                
                    
            return index 
        
        
        def findRight(nums):
            
            index = -1
            start = 0
            end = len(nums) - 1
            
            while start <= end:
                
                mid = start + (end - start) // 2
                
                if nums[mid] <= target:
                    
                    start = mid + 1
                    
                else:
                    end = mid - 1
                    
                if nums[mid] == target:
                    
                    index = mid
                    
            return index
            
        
        print(findRight(nums))
        return [findLeft(nums), findRight(nums)]
                    
                    
            
            
        

        
        
        
  