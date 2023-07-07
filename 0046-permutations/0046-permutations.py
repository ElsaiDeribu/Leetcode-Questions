class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        visited = set()
        perm = []

        def recur():
            
            if len(perm) == len(nums):
                ans.append(perm[:])
                return 
            
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    perm.append(nums[i])
                    visited.add(nums[i])
                    recur()
                    visited.remove(nums[i])
                    perm.pop()
            
        
     
        recur()
        
        return ans
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def recur(arr):
            
#             if len(arr) == 1:
#                 return [arr.copy()] 
            
#             result = []
            
#             for _ in range(len(arr)):
#                 temp = arr.pop(0)
#                 perms = recur(arr)
#                 arr.append(temp)
                
#                 for perm in perms:
#                     perm.append(temp)
                
#                 result.extend(perms)
               
#             return result
        
        
        
#         return recur(nums)