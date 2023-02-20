class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = mid = 0
        right = len(nums) - 1
        
        
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
                
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
                
            else:
                mid += 1
                
        
#         countSort
#         count = [0,0,0]
        
#         for i in nums:
#             count[i] += 1
            
#         ptr = 0    
#         for i in range(len(count)):
#              while count[i]:
#                     nums[ptr] = i
#                     ptr += 1
#                     count[i] -= 1
                    
                