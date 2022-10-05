class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
#         for i in range(1, len(nums)):
            
#             nums[i] = nums[i] + nums[i - 1]
        
#         i = 0
#         j= 0
#         minimum = 10**9 
#         sumation = nums[0]
#         print(nums)
        
#         while i < len(nums):
            
#             if minimum == 1 :
#                 return minimum
            
#             while sumation < target and j < len(nums):
                
#                 if i == 0:
#                     sumation = nums[j]
#                 else:
#                     sumation = nums[j] - nums[i - 1]
#                 if sumation < target:
#                     j += 1
                
#             while sumation >= target and i <= j:  
#                 if i == 0:
#                     sumation = nums[j]
#                 else:
#                     sumation = nums[j] - nums[i - 1]
#                 if sumation >= target:    
#                     i += 1
            
#             if sumation >= target:    
#                 length = (j - i + 1)
#                 minimum = min(minimum, length)

            
            
#         print(minimum)
        
    

            i = 0
            j = 0
            minLength = 10**9
            windowSum = nums[i]


            while j < len(nums):
                
                if minLength == 1:
                    return minLength
                
                while j < len(nums) and windowSum < target:
                    j += 1
                    if j < len(nums):
                        windowSum += nums[j]

                if windowSum >= target:
                    minLength = min(minLength, j - i + 1)

                while i < j and windowSum >= target:
                    windowSum -= nums[i]
                    i += 1
                    if windowSum >= target:
                        minLength = min(minLength, j - i + 1)
                        
            if minLength == 10**9:
                return 0
            return minLength

            
            
        
    
    
    
    
    
    
    
    
            
             
             
        