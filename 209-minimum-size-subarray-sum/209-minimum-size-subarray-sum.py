class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
         
         # prifix sum with sliding window solution
        
            for i in range(1,len(nums)):
                nums[i] = nums[i] + nums[i - 1]
                
            nums.insert(0,0)
            windowSum = nums[1]
            minLength = 10**9
            
            i = j = 1

            while j < len(nums):
                
                if minLength == 1:
                    return 1
                
                while j < len(nums) and windowSum < target:
                    
                    j += 1
                    if j < len(nums):
                        windowSum = nums[j] - nums[i - 1]
                        
                        
                if windowSum >= target:
                    minLength = min(minLength, j - i + 1)
                    
                    
                while i < j and windowSum >= target:
                    i += 1
                    windowSum = nums[j] - nums[i - 1]
                    
                    if windowSum >= target:
                        minLength = min(minLength, j - i + 1)
                
            if minLength == 10**9:
                return 0
            
            return minLength
        
        
        
        # sliding window solution
    
        
#             i = 0
#             j = 0
#             minLength = 10**9
#             windowSum = nums[i]


#             while j < len(nums):
                
#                 if minLength == 1:
#                     return minLength
                
#                 while j < len(nums) and windowSum < target:
#                     j += 1
#                     if j < len(nums):
#                         windowSum += nums[j]

#                 if windowSum >= target:
#                     minLength = min(minLength, j - i + 1)

#                 while i < j and windowSum >= target:
#                     windowSum -= nums[i]
#                     i += 1
#                     if windowSum >= target:
#                         minLength = min(minLength, j - i + 1)
                        
#             if minLength == 10**9:
#                 return 0
#             return minLength

            
            
        
    
    
    
    
    
    
    
    
            
             
             
        