class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixes = defaultdict(int)
        prefixes[0] = 1
        sum = 0
        count = 0
       
        
        for i in range (len(nums)):
            sum += nums[i]
            if sum - k in prefixes :
                count += prefixes[sum - k]
            prefixes[sum] += 1 
            
        return count
                
        
        
        
#         nums.sort()
#         counter, preSum, i, j = 0, 0, 0, 0
    
#         while j < len(nums):
#             while j < len(nums) and preSum < k:
#                 preSum += nums[j]
#                 j += 1
    
#             while i < len(nums) and preSum >= k:
#                 if preSum == k:
#                     counter += 1
#                 preSum -= nums[i]
#                 i += 1
            
#         return counter
        
        