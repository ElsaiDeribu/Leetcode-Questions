class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        for k in range(len(nums)):
            if nums[k] != 0:
                break
                
            if k == len(nums) - 1:
                return "0"
            
           
        
        
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                comb1 = int(str(nums[i]) + str(nums[j]))
                
                comb2 = int(str(nums[j]) + str(nums[i]))
                
                if comb2 > comb1:
                    nums[i], nums[j] = nums[j], nums[i]
                    
                    
        return ''.join(map(str, nums))
        