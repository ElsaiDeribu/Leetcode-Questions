class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def recur(arr):
            
            if len(arr) == 1:
                return [arr[:]] 
             
            result = []
            for i in range(len(arr)):
                n = arr.pop(0)
                nxt = recur(arr)
                arr.append(n)
                
                for item in nxt:
                    item.append(n)
                    
                    
                result.extend(nxt)
                
            return result
        
        
        return recur(nums)
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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