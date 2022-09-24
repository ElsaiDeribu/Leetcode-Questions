class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        l = 1
        r = l
        visited = set()
        visited.add(nums[0])
        
        while l < len(nums):
            
            r = l
            
            if nums[l] in visited:
                while r < len(nums) and nums[r] in visited:
                    r += 1
                    
                if r >= len(nums):
                    return l
                else:
                    # visited.add(nums[r])
                    nums[l], nums[r] = nums[r], nums[l]
                    
            visited. add(nums[l])   
            l += 1
            
            
            
        
#         i = 0
#         j = 1
#         visited = set()
        
#         if len(set(nums)) == len(nums):
            
#             return len(nums)
        
        
#         while i < len(nums) - 1:
            
#             visited.add(nums[i])
#             j = i + 1

#             # if nums[j] in visited:
#             while j < len(nums) and nums[j] in visited:
#                 j += 1

#             if j < len(nums) and nums[j] not in visited:   
#                 nums[i + 1], nums[j] = nums[j], nums[i + 1]

#             i += 1
            
            
#         return len(visited)

       
    
    
#         numbers = set(nums)
#         i = 0
#         for n in numbers:
#             nums[i] = n
#             i += 1
            
#         return len(numbers)