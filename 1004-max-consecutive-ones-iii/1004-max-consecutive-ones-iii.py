class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
#         right = 0
#         left = 0
#         largest = 0
        
#         while right < len(nums):
            
#             if nums[right] == 0 :
#                 k -= 1

#             while k < 0 :      
#                 if nums[left] == 0:
#                     k += 1
#                 left += 1
             
#             largest = max(largest, right - left + 1)                   
#             right += 1
                    
#         return largest


        r = 0
        l = 0
        intruder = 0
        longest = 0
        
        while l < len(nums):
            
            while r < len(nums) and (nums[r] == 1 or intruder < k):
                
                if nums[r] != 1:
                    intruder += 1
                    
                r += 1
                
            longest = max(longest, r - l)
            
            if nums[l] != 1:
                intruder -= 1
                
            l += 1
            
        return longest
                
    