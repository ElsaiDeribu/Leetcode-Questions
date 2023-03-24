class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def recur(start, end):
       
            pivot = start
            write = pivot + 1
            
#           find position
            for read in range(start + 1, end):
                if nums[pivot] > nums[read]:
                    nums[write], nums[read] = nums[read], nums[write]
                    write += 1 
                    
            nums[write - 1], nums[pivot]  = nums[pivot], nums[write - 1]
            
            if write - 1 == (len(nums) - k):
                return nums[write - 1]
             
            elif write - 1 > (len(nums) - k):
#               go left
                return recur(start, write - 1)
            
            else:
#               go right
                return recur(write , end)
                
              
            
        return recur(0, len(nums))
        
        
        
        
        
        