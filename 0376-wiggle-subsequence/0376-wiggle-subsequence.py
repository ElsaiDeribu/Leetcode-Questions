class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        count = 1
        last = nums[0]
        positive = None
        
        for i in range(1, len(nums)):
            
            curr = nums[i]
            
            if positive == None and curr - last != 0:
                positive = (curr - last > 0)
                last = curr
                count = 2

            elif curr - last > 0 and not positive:
                positive = not positive
                last = curr
                count += 1
                
            elif curr - last < 0 and positive:
                positive = not positive
                last = curr
                count += 1
                
            else:
                last = curr
                
                
        return count
                
                
            
            