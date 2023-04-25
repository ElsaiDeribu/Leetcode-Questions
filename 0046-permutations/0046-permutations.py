class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        perm = []
        visited = 2 ** len(nums)
        
        def dfs():
            if len(perm) == len(nums):
                ans.append(perm[:])
                return
            
            for i in range(len(nums)):
                nonlocal visited
                if not (1 << i & visited):
                    visited |= (1 << i)
                    perm.append(nums[i])
                    
                    dfs()
                    
                    visited = ~visited
                    visited |= (1 << i) 
                    visited = ~visited
                    perm.pop()
                    
                    
        dfs()
        
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